from django.db import models

import json, math, re
from urllib.request import urlopen


class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Scraper(object):
    URL = 'http://lda.data.parliament.uk/{dataset}.json?_pageSize=500&_page={page}'

    def __init__(self, dataset=None, excluded_keys=[]):
        assert dataset != None
        self.dataset = dataset
        self.excluded_keys = excluded_keys + ['_about', 'label']
        self.items = []
        self.cleaned_items = []
        page = self.get_page(0)
        self.count = page['result']['totalResults']
        self.add_items(page['result']['items'])
        self.num_pages = math.ceil(self.count/500)
        for i in range(1, self.num_pages):
            page = self.get_page(i)
            self.add_items(page['result']['items'])

    def camel_to_snake(self, name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def schema(self):
        '''
        return a dictionary with all the available keys and wether they are
        allowed to be blank or not.
        '''
        schema = set()
        for item in self.items:
            schema.update([key for key in item.keys()])
        schema = {field: 'required' for field in list(schema)}
        for item in self.items:
            for key in schema.keys():
                if key not in item.keys():
                    schema[key] = 'can_be_blank'
        pprint(schema)

    def add_items(self, items):
        for item in items:
            self.items.append(item)
            clean = {}
            for key in item.keys():
                if key not in self.excluded_keys:
                    if key == 'gender':
                        if item[key]['_value'] == 'Female':
                            clean[self.camel_to_snake(key)] = 'F'
                        elif item[key]['_value'] == 'Male':
                            clean[self.camel_to_snake(key)] = 'M'
                        else:
                            raise Exception('must have a gender')
                    elif isinstance(item[key], dict):
                        clean[self.camel_to_snake(key)] = item[key]['_value']
                    else:
                        clean[self.camel_to_snake(key)] = item[key]
            self.cleaned_items.append(clean)

    def get_page(self, page_number):
        url = self.URL.format(dataset=self.dataset, page=page_number)
        str_resp = urlopen(url).read().decode('utf-8')
        return json.loads(str_resp)
