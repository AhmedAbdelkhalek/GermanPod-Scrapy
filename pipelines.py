# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from urllib.request import urlretrieve


class GerpodPipeline(object):
    def process_item(self, item, spider):
        path = "src\\"

        item["word_id"] = item["img_url"].replace("_96square.jpg", "")
        item["word_id"] = "w" + item["word_id"].replace("https://d1pra95f92lrn3.cloudfront.net/media/thumb/", "")
        item["img_url"] = item["img_url"].replace("_96square.jpg", "_192square.jpg")
        urlretrieve(item["img_url"], path + item["word_id"] + '.jpg')

        urlretrieve(item["ger_word_sound_url"], path + item["word_id"] + "wg" + '.mp3')
        urlretrieve(item["eng_word_sound_url"], path + item["word_id"] + "we" + '.mp3')

        if item["ger_example_sound_url"]:
            urlretrieve(item["ger_example_sound_url"], path + item["word_id"] + "xg" + '.mp3')
            urlretrieve(item["eng_example_sound_url"], path + item["word_id"] + "xe" + '.mp3')

        return item
