import scrapy
from ..items import BasicSpiderItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

class BookSpider(scrapy.Spider):
    name = 'book_spider'

    start_urls = [
        'https://books.toscrape.com/'
    ]

    def parse(self, response):
        categories = response.css('.nav-list ul a::attr(href)').getall()
        
        yield from response.follow_all(categories, self.parse_categories)

    def parse_categories(self, response):

        for book in response.css('.col-lg-3'):
            loader = ItemLoader(item=BasicSpiderItem(), selector=book)
            loader.add_css('book_title', '.product_pod a::attr(title)')
            loader.add_css('book_price', '.price_color::text')
            loader.add_css('book_img_url', '.thumbnail::attr(src)', MapCompose(response.urljoin))
            loader.add_value('book_details_url', response.urljoin(book.css('.product_pod a::attr(href)').get()))

            yield loader.load_item()

        next_page = response.css('.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_categories)