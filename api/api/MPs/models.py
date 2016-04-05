from django.db import models

import json, math, re, uuid
from urllib.request import urlopen
from pprint import pprint


def camel_to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


class Scraper(object):
    MPs_URL = 'http://lda.data.parliament.uk/members.json?_pageSize=500&_page={}'
    count = None
    items = []
    cleaned_items = []
    num_pages = None
    excluded_keys = ['_about', 'label', 'constituency']

    def __init__(self):
        page = self.get_page(0)
        self.count = page['result']['totalResults']
        self.add_items(page['result']['items'])
        self.num_pages = math.ceil(self.count/500)
        for i in range(1, self.num_pages):
            page = self.get_page(i)
            self.add_items(page['result']['items'])

        #self.schema()

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
                            clean[camel_to_snake(key)] = 'F'
                        elif item[key]['_value'] == 'Male':
                            clean[camel_to_snake(key)] = 'M'
                        else:
                            raise Exception('must have a gender')
                    elif isinstance(item[key], dict):
                        clean[camel_to_snake(key)] = item[key]['_value']
                    else:
                        clean[camel_to_snake(key)] = item[key]
            self.cleaned_items.append(clean)

    def get_page(self, page_number):
        str_resp = urlopen(self.MPs_URL.format(page_number)).read().decode('utf-8')
        return json.loads(str_resp)

class MP(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    additional_name = models.CharField(max_length=1024, blank=True)
    home_page = models.URLField(blank=True)
    #constituency = models.ManyToManyField(Constituency, blank=True)
    family_name = models.CharField(max_length=1024)
    full_name = models.CharField(max_length=1024)
    gender = models.CharField(
        max_length=2,
        choices=(
            ('M','Male'),
            ('F','Female')
        )
    )
    given_name = models.CharField(max_length=1024, blank=True)
    party = models.CharField(max_length=512, blank=True)
    twitter = models.URLField(blank=True)
