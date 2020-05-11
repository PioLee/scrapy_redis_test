# -*- coding: utf-8 -*-
import scrapy_redis

# Scrapy settings for redis_test project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'redis_test'

SPIDER_MODULES = ['redis_test.spiders']
NEWSPIDER_MODULE = 'redis_test.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'redis_test (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

""" scrapy-redis配置 """
# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
REDIS_URL = "redis://@127.0.0.1:6379"
# 在redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复，也就是不清理redis queues
# 不清除Redis队列、这样可以暂停/恢复 爬取
SCHEDULER_PERSIST = True
# 每次运行爬虫就会重载
SCHEDULER_FLUSH_ON_START = False
# 爬虫运行超过设定时间，如果爬虫还没有结束，则自动关闭
CLOSESPIDER_TIMEOUT = 5

# Mongodb配置
MONGO_DB_URI = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'oalur'

# 延时等待
DOWNLOAD_DELAY = 0

# 重试次数
RETRY_ENABLED = True
RETRY_TIMES = 3

# cookie操作
COOKIES_ENABLED = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 10
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     # "Host": "www.netsea.jp",
#     "cookie": "cna=8fXvFVBr8VsCAXkjAERq2rQZ; tg=0; tracknick=%5Cu4F50%5Cu5E0C609; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=Esvsim8XjQVCJdxoU8uNi; uc3=lg2=W5iHLLyFOGW7aA%3D%3D&vt3=F8dBxd9nXEmrWRuHzZo%3D&id2=Uone9%2Frg1aIz4A%3D%3D&nk2=tOvz67sIFg%3D%3D; lgc=%5Cu4F50%5Cu5E0C609; uc4=id4=0%40UOE0DQEfEdHmnz97oDzxznpUDYPU&nk4=0%40tg0uFsyZI0%2B0nAMuQu1X1%2BLZ; _cc_=Vq8l%2BKCLiw%3D%3D; enc=2VTWVY6IVd0B3icMyzPZM41KgDHsXOjLWY7dFF7HyPdLIzJ0WIALys1NOgqL6%2FQ3LTDHgW5x2U8l27gkahy5dw%3D%3D; tfstk=c4rGBima1Pu1w_L2PFi_H0C31ISRa0-qZorQYluCCvg0wpqEQsDD8UkRT9cGnvYf.; mt=ci=-1_0; v=0; cookie2=16fa007cf580fbf122a5724644cdf5a1; t=13d521445baec5651024bd50eb5c9013; _tb_token_=e534386bb7eeb; _m_h5_tk=df077aace64c0432b66642cbd42019c5_1585651150373; _m_h5_tk_enc=09d2fb66c6a0c096d7d25edd7a24fb61; l=dBT_pm_nQyuYz9gBBOCNdFlV4pQOSIRAguJw01OJi_5IK1Ls2d_Oosznnep6VjWfTjYB4vOVfvy9-etkq3DmndH8sxAJwxDc.; isg=BCcnD_yyNby4LrHDEzY93WmWtlvxrPuONV_5__mUQ7bd6EeqAXyL3mXqCuj2ANMG; uc1=cookie14=UoTUP2R4jAyqnQ%3D%3D",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'redis_test.middlewares.RedisTestSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'redis_test.middlewares.RedisTestDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'redis_test.pipelines.RedisTestPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 300,
    # 'oalur.pipelines.OalurPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
