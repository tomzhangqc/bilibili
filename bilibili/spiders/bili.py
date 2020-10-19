# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class BiliSpider(scrapy.Spider):
    name = 'bili'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/ranking/bangumi/13/1/3']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, args={'wait': 2})

    def parse(self, response):
        nums = response.xpath("//div[@id='app']//div[@class='num']/text()").extract()
        titles = response.xpath("//div[@id='app']//div[@class='info']/a/text()").extract()
        scores = response.xpath("//div[@id='app']//div[@class='pts']/div/text()").extract()
        for num, title, score in zip(nums, titles, scores):
            yield {
                'num': num,
                'title': title,
                'score': score
            }
