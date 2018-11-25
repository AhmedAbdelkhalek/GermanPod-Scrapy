# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join

# this class will be used to process the scraped data,
class WordLoader(ItemLoader):
    # still not sure, but scrapy deals with items as lists,
    # and urls are required to be texts to be downloaded, so we join the urls for the pipelines module to usu them.
    img_url_out = Join("")
    word_id_out = Join("")
    ger_word_sound_url_out = Join("")
    eng_word_sound_url_out = Join("")
    ger_example_sound_url_out = Join("")
    eng_example_sound_url_out = Join("")


class GerpodItem(scrapy.Item):
    # define the fields for your item here like:    # standard scrapy structure.
    img_url = scrapy.Field()
    word_id = scrapy.Field()
    ger_word_article = scrapy.Field()
    ger_word = scrapy.Field()
    ger_word_sound_url = scrapy.Field()
    eng_word = scrapy.Field()
    eng_word_sound_url = scrapy.Field()
    ger_example = scrapy.Field()
    ger_example_sound_url = scrapy.Field()
    eng_example = scrapy.Field()
    eng_example_sound_url = scrapy.Field()
