import scrapy
import re
import time
from zhuewang.items import ZhuewangItem

class ZhuewanghqSpider(scrapy.Spider):
    name = 'zhuewanghq'
    allowed_domains = ['zhue.com.cn']
    url_value = 'https://cj.zhue.com.cn/shichangfenxi/108-'
    url_index = 1
    url_index2 = '.html'
    start_urls = [url_value + str(url_index)+url_index2]

    def parse(self, response):
        #取出每个帖子的子url
        web_url = response.xpath("//h3//a/@href")  # 取他的href属性
        for url in web_url:
            new_url = url.get()  # 得到了子URL
            yield scrapy.Request(new_url, callback=self.parse_item,
                                 dont_filter=True)  # 这里有个坑，就是要加上dont_filter=True 才会输出response.url
        #设置页码终止条件
        if self.url_index <= 10:
            self.url_index += 1
            yield scrapy.Request(self.url_value + str(self.url_index)+(self.url_index2), callback=self.parse, dont_filter=True) #一定要记得加self
            print("---------------------"+str(self.url_index)+'页'+"---------------------")
            #time.sleep(5)
        pass
    def parse_item(self, response):
        #创建自定对象
        item_dic = ZhuewangItem()
        # 存储字典,键值对
        item_dic["title"] = response.xpath("//div[@class='ebDet_nBor']//h1").xpath('string(.)').extract()
        item_dic["time"] = response.xpath("//p[@class='writ']//span[3]").xpath('string(.)').extract() #层级标签
        item_dic["content"] ='\n'.join(response.xpath("//div[@id='art_content']//p").xpath('string(.)').extract())
        #print(item_dic)
        yield item_dic #这样的话就需要在piplines里面print(item),同时在settings里面“ctrl+/”打开ITEM_PIPELINES
