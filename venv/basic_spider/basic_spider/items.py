# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BasicSpiderItem(scrapy.Item):
    book_title = scrapy.Field()
    book_price = scrapy.Field()
    book_img_url = scrapy.Field()
    book_details_url = scrapy.Field()
