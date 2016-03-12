# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HansardComment(scrapy.Item):
    # define the fields for your item here like:
    author_id = scrapy.Field()
    author_name = scrapy.Field()
    house = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()
