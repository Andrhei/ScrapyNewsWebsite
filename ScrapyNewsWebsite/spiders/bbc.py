import scrapy
import json

class BBCSpider(scrapy.Spider):
    name = "bbc"
    start_urls=[]
    
    with open('search.json', 'r') as url_list:
        url_list = json.loads(url_list.read())
    for element in url_list:
        start_urls.append(element['url'])

    def parse(self, response):
        page_title = response.css('title::text').get()
        items = response.css('.gs-c-promo')
        for item in items:
            news = {
                "page_title":page_title,
                "head":item.css('.gs-c-promo-heading__title::text').get(),
                "tag":item.css('.gs-c-section-link span::text').get(),
                "url_news":item.css('.gs-c-promo-heading::attr(href)').get(),
                "media_url":item.css('.gs-o-responsive-image img::attr(src)').get(),
                "date_time":item.css('.gs-o-bullet__text::attr(datetime)').get()
            }
            yield news
