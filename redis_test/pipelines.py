# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy import Item


class RedisTestPipeline(object):
    def process_item(self, item, spider):
        return item


class OalurPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        cls.DB_URL = crawler.settings.get('MONGO_DB_URI', 'mongodb://localhost:27017')
        cls.DB_NAME = crawler.settings.get('MONGO_DB_NAME', 'oalur')
        return cls()

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.DB_URL)
        self.db = self.client[self.DB_NAME]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # collection = self.db['product']
        collection = self.db['test']
        post = dict(item) if isinstance(item, Item) else item
        collection.update_one({"asin": item['asin']}, {"$set": post}, upsert=True)
        print('存储成功', item['asin'])
        return item
