# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request
from ..items import BaidupicItem


class PicSpider(scrapy.Spider):
    name = 'pic'
    allowed_domains = ['image.baidu.com']
    start_urls = ['http://image.baidu.com/']

    search_keyword = '抽象画'
    ajax_demo_url = r'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%8A%BD%E8%B1%A1%E7%94%BB&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=0&ic=0&word=%E6%8A%BD%E8%B1%A1%E7%94%BB&s=&se=&tab=&width=0&height=0&face=0&istype=2&qc=&nc=&fr=&pn=120&rn=30&gsm=78&1509201569349='
    ajax_base_url = r'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%8A%BD%E8%B1%A1%E7%94%BB&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=0&ic=0&word=%E6%8A%BD%E8%B1%A1%E7%94%BB&s=&se=&tab=&width=0&height=0&face=0&istype=2&qc=&nc=&fr=&pn=120&rn=30&gsm=78&150920'

    @classmethod
    def url_from_index(cls, index: int):
        """index should be a 7-digit integer starts with 10"""
        return cls.ajax_base_url + str(index) + '='

    def parse(self, response):
        """dummy starter"""
        for i in range(1000000, 2500000, 1):
            url = self.url_from_index(i)
            yield Request(url, callback=self.parse_ajax)

    def parse_ajax(self, response):
        js = json.loads(response.body)
        data = js['data']
        for obj in data:
            replace_url = obj['replaceUrl']
            pic_url = replace_url[0]['ObjURL']

            item = BaidupicItem()
            item['url'] = pic_url
            item['referrer'] = response.url
            yield item
