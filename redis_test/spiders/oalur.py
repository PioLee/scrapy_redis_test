# -*- coding: utf-8 -*-
import logging
import scrapy
import time
import json
import datetime

from scrapy_redis.spiders import RedisSpider

from redis_test.items import OalurItem


class OalurSpiderSpider(RedisSpider):
    name = 'oalur_spider'
    # allowed_domains = ['www.oalur.com']
    headers = {
        'cookie': 'EGG_SESS=DxAY67OorWEe0naxz4ZDoZn8yaoARbA5Vr6vs9vnoPYih8VKqstrl3Q6oLfoN8-C',
        'Content-Type': 'application/json',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
    }

    def start_requests(self):
        t = str(time.time()).replace(r'.', "")[:13]
        url = "https://www.oalur.com/api/products?t={}".format(t)
        # for i in range(1, 101):
        params = {"pageNum": 1, "pageSize": 100, "searchKey": "keyword", "searchValue": "", "granularity": "d1",
                  "sortBy": "saleNum", "desc": True, "categoryPath": "", "categoryFeature": None,
                  "advancedParams": {},
                  "keywordParams": {}}
        yield scrapy.Request(url, callback=self.detail, method='POST', body=json.dumps(params),
                             headers=self.headers)

    # 获取所有产品基本信息
    def detail(self, response):
        print(response.text)
        print(response.url)
        # logging.info(f'商品搜索页面地址{response.url}')
        data = json.loads(response.text)
        if data['message'] == "ok":
            for value in data['data']['results']:
                item = OalurItem()
                asin = value.get('asin')
                item['asin'] = asin
                item['name'] = value.get('title')
                item['saleNum'] = value.get('saleNum')
                item['lastBsr'] = value.get('lastBsr')
                item['totalCommentNum'] = value.get('totalCommentNum')
                item['score'] = value.get('score')
                item['price'] = value.get('price')
                item['sellerNum'] = value.get('sellerNum')
                item['generateDate'] = value.get('generateDate')
                item['update_time'] = datetime.datetime.utcnow()
                t = str(time.time()).replace(r'.', "")[:13]
                url = 'https://www.oalur.com/api/products/details?t={}&asin={}'.format(t, asin)
                yield scrapy.Request(url, callback=self.point, meta={'item': item}, headers=self.headers)

    # 获取产品要点
    def point(self, response):
        data = json.loads(response.text)
        t = str(time.time()).replace(r'.', "")[:13]
        point = data['data']['bulletPoints']
        if data['message'] == "ok":
            item = response.meta['item']
            item['points'] = point
            url = "https://www.oalur.com/api/keywords?t={}&asin={}&pageNum=1&sortBy=focus&desc=false".format(t, item[
                'asin'])
            yield scrapy.Request(url, callback=self.keywords, meta={'item': item}, headers=self.headers)

    # 获取产品关键词作为参数获取产品全景动态BSR排名
    def keywords(self, response):
        data = json.loads(response.text)
        t = str(time.time()).replace(r'.', "")[:13]
        if data['message'] == "ok":
            item = response.meta['item']
            kwd = list()
            for value in data['data']['results'][:5]:
                kwd.append(value.get('keyword'))
            asin = item['asin']
            params = {"asin": asin, "label": False,
                      "selectKeywords": kwd}
            url = 'https://www.oalur.com/api/products/milestoneGraph?t={}'.format(t)
            yield scrapy.Request(url, callback=self.parse, method='POST', meta={'item': item}, headers=self.headers,
                                 body=json.dumps(params), )

    def parse(self, response):
        data = json.loads(response.text)
        if data['message'] == "ok":
            date = data['data']['date'][-7:]
            bsr = data['data']['bsr'][-7:]
            miles = dict(zip(date, bsr))
            item = response.meta['item']
            item['detail'] = miles
            yield item
