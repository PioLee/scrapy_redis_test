# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RedisTestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class OalurItem(scrapy.Item):
    # collection = 'product'  # Mongodb集合名
    saleNum = scrapy.Field()  # 预计月销量
    lastBsr = scrapy.Field()  # 最新热销产品排名
    totalCommentNum = scrapy.Field()  # 产品评论数
    totalCommentVolume = scrapy.Field()  # 产品评论1天变化
    score = scrapy.Field()  # 评分
    price = scrapy.Field()  # 产品价格
    generateDate = scrapy.Field()  # 上架时间
    sellerNum = scrapy.Field()  # 卖家数量
    name = scrapy.Field()  # 产品名
    asin = scrapy.Field()  # 产品ASIN
    points = scrapy.Field()  # 产品要点
    detail = scrapy.Field()  # 产品最近七天的BSR排名
    update_time = scrapy.Field()  # 更新时间
