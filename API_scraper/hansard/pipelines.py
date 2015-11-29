# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from nltk.corpus import stopwords
import re
from bs4 import BeautifulSoup


class CleanText(object):
    def process_item(self, item, spider):
        item['content'] = self.clean_content(item['content'])
        return item

    def clean_content(self, text):
        # 2. Remove non-letters
        letters_only = re.sub("[^a-zA-Z]", " ", text)

        # 3. Convert to lower case, split into individual words
        words = letters_only.lower().split()

        # 4. In Python, searching a set is much faster than searching
        #   a list, so convert the stop words to a set
        stops = set(stopwords.words("english"))

         # 5. Remove stop words
        meaningful_words = [w for w in words if not w in stops]

        # 6. Join the words back into one string separated by space,
        # and return the result.
        return( " ".join( meaningful_words ))
