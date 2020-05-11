# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider


class TestSpider(RedisSpider):
    name = 'test'
    # allowed_domains = []
    # start_urls = ['https://item.taobao.com/item.htm?spm=a217f.8051907.312171.33.2df233088ZDEBU&id=561043847738']
    redis_key = 'tests:start_urls'

    def parse(self, response):
        print(response.url)
