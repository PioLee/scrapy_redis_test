from scrapy.cmdline import execute

name = 'oalur_spider'
cmd = 'scrapy crawl {0}'.format(name)
execute(cmd.split())

