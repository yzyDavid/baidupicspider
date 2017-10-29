# -*- coding: utf-8 -*-
import scrapy


class BingpicSpider(scrapy.Spider):
    name = 'bingpic'
    allowed_domains = ['cn.bing.com']
    start_urls = ['http://cn.bing.com/']

    ajax_urls = [
        'https://cn.bing.com/images/async?q=%e6%8a%bd%e8%b1%a1%e7%94%bb&first=81&count=35&relp=35&lostate=r&mmasync=1&dgState=x*0_y*0_h*0_c*5_i*71_r*13&IG=1ECA2F54576D4683A699D05E6241DB54&SFX=3&iid=images.5761',
        'https://cn.bing.com/images/async?q=%e6%8a%bd%e8%b1%a1%e7%94%bb&first=118&count=35&relp=35&lostate=r&mmasync=1&dgState=x*284_y*1207_h*192_c*1_i*106_r*20&IG=1ECA2F54576D4683A699D05E6241DB54&SFX=4&iid=images.5761',
        '',
    ]

    def parse(self, response):
        pass
