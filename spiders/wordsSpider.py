# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from ..items import GerpodItem
from ..items import WordLoader


def word_extract(tag, css_class):
    tag = tag.find(attrs={"class": css_class})
    if tag:
        return tag.find("span").text
    return ""


def sound_url_extract(tag, css_class):
    tag = tag.find(attrs={"class": css_class})
    if tag:
        return tag.find("audio")["src"]
    return ""


class WordsSpider(scrapy.Spider):
    name = 'wordsSpider'
    allowed_domains = ['www.germanpod101.com']
    start_urls = ['https://www.germanpod101.com/german-word-lists/']
    id = 0

    def parse(self, response):
        soup = BeautifulSoup(response.body, "html.parser")
        item_boxes = soup.find_all(attrs={"class": "wlv-item__box"})

        for item_box in item_boxes:
            loader = WordLoader(item=GerpodItem())
            # id += 1
            # loader.add_value("word_id", "w{}".format(id))
            loader.add_value("img_url", item_box.find("img")["src"])

            loader.add_value("ger_word", word_extract(item_box, "wlv-item__word-container"))
            loader.add_value("ger_word_sound_url", sound_url_extract(item_box, "wlv-item__word-container"))
            loader.add_value("eng_word", word_extract(item_box, "wlv-item__english-container"))
            loader.add_value("eng_word_sound_url", sound_url_extract(item_box, "wlv-item__english-container"))

            ger_word_article = item_box.find("span", attrs={"class": "wlv-item__word-article"})
            loader.add_value("ger_word_article", ger_word_article.text if ger_word_article else "")

            example_box = item_box.find(attrs={"class": "wlv-item__samples-box"})
            loader.add_value("ger_example", word_extract(example_box, "wlv-item__word-container"))
            loader.add_value("ger_example_sound_url", sound_url_extract(example_box, "wlv-item__word-container"))
            loader.add_value("eng_example", word_extract(example_box, "wlv-item__english-container"))
            loader.add_value("eng_example_sound_url", sound_url_extract(example_box, "wlv-item__english-container"))

            yield loader.load_item()

            next_page_ref = soup.find(attrs={"class": "r101-pagination--b"}).find_all("a")[-1]["href"]
            yield Request(url="https://www.germanpod101.com/german-word-lists/" + next_page_ref)
