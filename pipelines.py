# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# use it to download resources in an easy way.
from urllib.request import urlretrieve

# pipe line is activated in the settings module
class GerpodPipeline(object):
    def process_item(self, item, spider):
        path = "src\\"  # storing folder path, feel free to change it.

        # urls for images would be like this
        # https://d1pra95f92lrn3.cloudfront.net/media/thumb/9622_96square
        # it's required to get the id "9622"
        # also better to download the bigger size image, so, replace _96square with _192square
        # I know that it can be done RE, but I prefer that for now for readability.
        item["word_id"] = item["img_url"].replace("_96square.jpg", "")
        item["word_id"] = "w" + item["word_id"].replace("https://d1pra95f92lrn3.cloudfront.net/media/thumb/", "")
        item["img_url"] = item["img_url"].replace("_96square.jpg", "_192square.jpg")
        # download the image and rename it
        urlretrieve(item["img_url"], path + item["word_id"] + '.jpg')

        # download the sounds and rename them
        urlretrieve(item["ger_word_sound_url"], path + item["word_id"] + "wg" + '.mp3')
        urlretrieve(item["eng_word_sound_url"], path + item["word_id"] + "we" + '.mp3')

        # only if example is exist, download the example sounds and rename them
        if item["ger_example_sound_url"]:
            urlretrieve(item["ger_example_sound_url"], path + item["word_id"] + "xg" + '.mp3')
            urlretrieve(item["eng_example_sound_url"], path + item["word_id"] + "xe" + '.mp3')

        return item
