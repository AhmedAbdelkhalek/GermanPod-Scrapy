# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GerpodItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    word_id = scrapy.Field()
    img_url = scrapy.Field()
    ger_word_article = scrapy.Field()
    ger_word = scrapy.Field()
    ger_word_sound_url = scrapy.Field()
    eng_word = scrapy.Field()
    eng_word_sound_url = scrapy.Field()
    ger_example = scrapy.Field()
    ger_example_sound_url = scrapy.Field()
    eng_example = scrapy.Field()
    eng_example_sound_url = scrapy.Field()
