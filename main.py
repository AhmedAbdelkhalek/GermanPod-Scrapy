from scrapy.cmdline import execute

execute("scrapy crawl wordsSpider -o words.csv".split())
