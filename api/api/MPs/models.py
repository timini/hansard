from django.db import models

import json, math
from urllib.request import urlopen



# Create your models here.

class MP(object):
    MPs_URL = 'http://lda.data.parliament.uk/members.json?_pageSize=500&_page={}'
    count = None
    items = []
    num_pages = None

    def __init__(self):
        page = self.get_page(0)
        self.count = page['result']['totalResults']
        self.items.extend(page['result']['items'])
        self.num_pages = math.ceil(self.count/500)
        for i in range(1, self.num_pages):
            page = self.get_page(i)
            self.items.extend(page['result']['items'])

    def get_page(self, page_number):
        str_resp = urlopen(self.MPs_URL.format(page_number)).read().decode('utf-8')
        return json.loads(str_resp)
