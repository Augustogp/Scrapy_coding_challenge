import scrapy
from scrapy_splash import SplashRequest
from ..items import JavascriptSpiderItem
from scrapy.loader import ItemLoader

class JSQuotesSpider(scrapy.Spider):
    name = 'js_quotes'
    def start_requests(self):
        yield SplashRequest(
                    url = 'https://quotes.toscrape.com/js/',
                    callback = self.parse
                )


    def parse(self, response):
        for quotes in response.css('.quote'):
            loader = ItemLoader(item=JavascriptSpiderItem(), selector=quotes)
            loader.add_css('quote', '.text::text')
            loader.add_css('author', '.author::text')
            loader.add_css('tags', '.tag::text')

            yield loader.load_item()

        next_page = response.css('.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield SplashRequest(url=next_page, callback=self.parse)

        

