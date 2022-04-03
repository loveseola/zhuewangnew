# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhuewangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #Scrapy.Field类就是内置dict类的一个子类
    title = scrapy.Field()
    # 每个帖子的时间
    time = scrapy.Field()
    # 每个帖子的内容
    content = scrapy.Field()

    pass
