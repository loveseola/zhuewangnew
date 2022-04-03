# -*- coding: utf-8 -*-
import re
from openpyxl import Workbook
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ZhuewangPipeline(object):
    def __init__(self): #定义一些需要初始化的方法
        self.wb = Workbook()
        self.ws = self.wb.active
        #设置表头
        self.ws.append(['标题','时间','内容'])
    def process_item(self, item, spider):
        title_str = item['title']
        time_str = item["time"]
        time_str = re.sub(r'[^0-9]', '', str(time_str))[0:8]
        content_str = item["content"]
        line = [title_str[0], time_str, content_str]
        self.ws.append(line)
        self.wb.save('zhuewangruiqi.xlsx')
        print("正在保存...")
        return item

    def close_spider(self, spider):
        print("爬取完毕！")
        spider.crawler.engine.close_spider(spider, '没有新数据关闭爬虫')



