# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class BilibiliPipeline(object):

    def open_spider(self, spider):
        self.mongo_client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.mongo_client.bilibili.rank.insert_one(item)
        return item

    def close_spider(self, spider):
        self.mongo_client.close()
