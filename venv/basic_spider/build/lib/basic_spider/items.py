# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose

def remove_pound_symbol(price):
    price = price.strip(u'\u00a3')
    return price

class BasicSpiderItem(scrapy.Item):
    book_title = scrapy.Field()
    book_price = scrapy.Field(
        input_processor = MapCompose(remove_pound_symbol)
        )
    book_img_url = scrapy.Field()
    book_details_url = scrapy.Field()
