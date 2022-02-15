import scrapy
from scrapy_splash import SplashRequest
from ..items import JavascriptSpiderItem

class JSQuotesSpider(scrapy.Spider):
    name = 'js_quotes'
    def start_requests(self):
        yield SplashRequest(
                    url = 'https://quotes.toscrape.com/js/',
                    callback = self.parse
                )


    def parse(self, response):
        item = JavascriptSpiderItem()

        for quotes in response.css('.quote'):
            item['quote'] = quotes.css('.text::text').get()
            item['author'] = quotes.css('.author::text').get()
            item['tags'] = quotes.css('.tag::text').getall()

            yield item

        next_page = response.css('.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield SplashRequest(url=next_page, callback=self.parse)

        

