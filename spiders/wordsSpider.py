# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

class WordsSpider(scrapy.Spider):
    name = 'wordsSpider'
    allowed_domains = ['www.germanpod101.com']
    start_urls = ['https://www.germanpod101.com/german-word-lists/']

    def parse(self, response):
        soup = BeautifulSoup(response.body, "html.parser")
        word_box = soup.find_all("", {"class": "wlv-item__box"})
        print(response.url)
             