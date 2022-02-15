import scrapy
from ..items import BasicSpiderItem

class BookSpider(scrapy.Spider):
    name = 'book_spider'

    start_urls = [
        'https://books.toscrape.com/'
    ]

    def parse(self, response):
        categories = response.css('.nav-list ul a::attr(href)').getall()
        
        yield from response.follow_all(categories, self.parse_categories)

    def parse_categories(self, response):

        item = BasicSpiderItem()

        for book in response.css('.col-lg-3'):
            item['book_title'] = book.css('.product_pod a::text').get()
            item['book_price'] = book.css('.price_color::text').get()
            item['book_img_url'] = response.urljoin(book.css('.thumbnail::attr(src)').get())
            item['book_details_url'] = response.urljoin(book.css('.product_pod a::attr(href)').get())

            yield item

        next_page = response.css('.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_categories)