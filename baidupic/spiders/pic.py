# -*- coding: utf-8 -*-
import scrapy


class PicSpider(scrapy.Spider):
    name = 'pic'
    allowed_domains = ['image.baidu.com']
    start_urls = ['http://image.baidu.com/']

    def parse(self, response):
        pass
