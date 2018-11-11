# -*- coding: utf-8 -*-
import scrapy


class WordsSpider(scrapy.Spider):
    name = 'wordsSpider'
    allowed_domains = ['www.germanpod101.com']
    start_urls = ['https://www.germanpod101.com/german-word-lists/']

    def parse(self, response):
        pass
