# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidupicItem(scrapy.Item):
    url = scrapy.Field()
    image_hash = scrapy.Field()
    referrer = scrapy.Field()
