# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request
from ..items import BaidupicItem
from lxml import etree
from IPython import embed


class PicSpider(scrapy.Spider):
    name = 'pic'
    allowed_domains = ['image.baidu.com']
    start_urls_ajax = ['http://image.baidu.com/']
    start_urls = [
        'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E6%8A%BD%E8%B1%A1%E7%94%BB&ct=201326592&ic=0&lm=-1&width=&height=&v=flip']
    base_url = 'https://image.baidu.com'

    search_keyword = '抽象画'  # not used
    ajax_demo_url = r'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%8A%BD%E8%B1%A1%E7%94%BB&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=0&ic=0&word=%E6%8A%BD%E8%B1%A1%E7%94%BB&s=&se=&tab=&width=0&height=0&face=0&istype=2&qc=&nc=&fr=&pn=120&rn=30&gsm=78&1509201569349='
    ajax_base_url = r'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%8A%BD%E8%B1%A1%E7%94%BB&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=0&ic=0&word=%E6%8A%BD%E8%B1%A1%E7%94%BB&s=&se=&tab=&width=0&height=0&face=0&istype=2&qc=&nc=&fr=&pn=120&rn=30&gsm=78&150920'

    img_xpath = '//*[@id="imgid"]/ul/li[8]/a/img'  # FIXME
    next_page_xpath = '//*[@id="page"]/a/@href'

    entries_per_page = 20

    @classmethod
    def url_from_index(cls, index: int):
        """index should be a 7-digit integer starts with 10"""
        return cls.ajax_base_url + str(index) + '='

    def parse(self, response):
        """by pages, starter"""
        sel = etree.HTML(response.body)
        next_page = sel.xpath(self.next_page_xpath)[-1]
        next_page = self.base_url + next_page
        yield Request(next_page, callback=self.parse)

    @DeprecationWarning
    def parse_ajax_start(self, response):
        """dummy starter"""
        for i in range(2500000, 1000000, -1):
            url = self.url_from_index(i)
            yield Request(url, callback=self.parse_ajax_waterfall)

    @DeprecationWarning
    def parse_ajax_waterfall(self, response):
        js = json.loads(response.body)
        data = js['data']
        for obj in data:
            replace_url = obj['replaceUrl']
            pic_url = replace_url[0]['ObjURL']

            item = BaidupicItem()
            item['url'] = pic_url
            item['referer'] = response.url
            yield item
