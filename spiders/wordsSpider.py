# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from ..items import GerpodItem, WordLoader  # import the items module for the scraper


def word_extract(tag, css_class):
    # a helper function to get the word text out of tags
    # accepts the full html tag and the class name for the text
    tag = tag.find(attrs={"class": css_class})
    if tag:
        return tag.find("span").text
    return ""


def sound_url_extract(tag, css_class):
    # a helper function to get the word sound url out of tags
    # accepts the full html tag and the class name for the sound url
    tag = tag.find(attrs={"class": css_class})
    if tag:
        return tag.find("audio")["src"]
    return ""

# scrapy the free 100 words in germanpod, 5 pages
class WordsSpider(scrapy.Spider):  # inherits from a scrapy basic spider.
    name = 'wordsSpider'
    allowed_domains = ['www.germanpod101.com']
    start_urls = ['https://www.germanpod101.com/german-word-lists/']

    id = 0

    # the main and only parser, works after the start_urls Request
    def parse(self, response):
        soup = BeautifulSoup(response.body, "html.parser")
        # get list of tags, each tag represents the html for a word
        # each tag contains the word + Sound in English and German, an image for the word, an Example in English and German
        item_boxes = soup.find_all(attrs={"class": "wlv-item__box"})

        # loop over tags to extract words, image, and sounds
        for item_box in item_boxes:
            # use the prepared items module to be able to download the resources.
            loader = WordLoader(item=GerpodItem())
            # find the img url
            loader.add_value("img_url", item_box.find("img")["src"])

            # find the word text and sound, English and German
            loader.add_value("ger_word", word_extract(item_box, "wlv-item__word-container"))
            loader.add_value("ger_word_sound_url", sound_url_extract(item_box, "wlv-item__word-container"))
            loader.add_value("eng_word", word_extract(item_box, "wlv-item__english-container"))
            loader.add_value("eng_word_sound_url", sound_url_extract(item_box, "wlv-item__english-container"))

            # get the article of the german word if it's a noun (Der, Das, Die)
            ger_word_article = item_box.find("span", attrs={"class": "wlv-item__word-article"})
            loader.add_value("ger_word_article", ger_word_article.text if ger_word_article else "")

            # in the paid version, a word can have many examples, here we just need the first one,
            # so we use "find" method
            example_box = item_box.find(attrs={"class": "wlv-item__samples-box"})
            # find the example text and sound, English and German
            loader.add_value("ger_example", word_extract(example_box, "wlv-item__word-container"))
            loader.add_value("ger_example_sound_url", sound_url_extract(example_box, "wlv-item__word-container"))
            loader.add_value("eng_example", word_extract(example_box, "wlv-item__english-container"))
            loader.add_value("eng_example_sound_url", sound_url_extract(example_box, "wlv-item__english-container"))

            # to let the item loader use them.
            yield loader.load_item()

            # the first page cotains only 20 or 25 words, so we find the next page and make a Request.
            # find the tag for the next page
            next_page_ref = soup.find(attrs={"class": "r101-pagination--b"}).find_all("a")[-1]["href"]
            yield Request(url="https://www.germanpod101.com/german-word-lists/" + next_page_ref)
