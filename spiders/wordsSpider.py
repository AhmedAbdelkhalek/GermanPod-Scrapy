# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class WordsSpider(scrapy.Spider):
    name = 'wordsSpider'
    allowed_domains = ['www.germanpod101.com']
    start_urls = ['https://www.germanpod101.com/german-word-lists/']

    def parse(self, response):
        soup = BeautifulSoup(response.body, "html.parser")
        item_boxes = soup.find_all(attrs={"class": "wlv-item__box"})
        for item_box in item_boxes:
            ger_word_box = item_box.find(attrs={"class": "wlv-item__word-container"})
            ger_word = ger_word_box.find("span").text
            ger_word_sound_url = ger_word_box.find("audio")["src"]

            eng_word_box = item_box.find(attrs={"class": "wlv-item__english-container"})
            eng_word = eng_word_box.find("span").text
            eng_word_sound_url = eng_word_box.find("audio")["src"]
 