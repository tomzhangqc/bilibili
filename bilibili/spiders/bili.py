# -*- coding: utf-8 -*-
import scrapy


class BiliSpider(scrapy.Spider):
    name = 'bili'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/ranking/bangumi/13/1/3']

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
