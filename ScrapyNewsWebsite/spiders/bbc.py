import scrapy


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
                "imageUrl": item.css('.responsive-image img::attr(src)').get()
            })
        print(news)
