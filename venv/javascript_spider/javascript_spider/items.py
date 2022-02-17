# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose

def remove_quotes(text):
    #strip unicode quotes
    text = text.strip(u'\u201c'u'\u201d')
    return text

class JavascriptSpiderItem(scrapy.Item):
    quote = scrapy.Field(
        input_processor=MapCompose(remove_quotes)
        )
    author = scrapy.Field()
    tags = scrapy.Field()

