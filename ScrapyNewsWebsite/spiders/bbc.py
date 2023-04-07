import scrapy
import re


class BBCSpider(scrapy.Spider):
    name = "bbc"

    def start_requests(self):
        url = "https://www.bbc.com/"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        news = []
        items = response.css('li.media-list__item') 
        for item in items:
            news.append({
                "image_url": item.css('.responsive-image img::attr(src)').get(),
                "head_line": re.sub("\n", "", str(item.css('.media__link::text').get())),
                "tag": str(item.css('.media__tag::text').get())
            })
        print(f'------------------>>{news[0]}<<-----------------')
