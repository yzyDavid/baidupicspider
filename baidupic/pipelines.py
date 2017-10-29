# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import re


class BaidupicPipeline(object):
    def process_item(self, item, spider):
        return item


class BaiduPicImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['url'], headers={'Referer': item['referer']})

    def item_completed(self, results, item, info):
        success, result = results[0]
        if not success:
            raise DropItem("Item contains no images")
        item['image_hash'] = re.search('/(.+)\.jpg', result['path']).group(1)
        return item
