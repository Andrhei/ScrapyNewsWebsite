import scrapy
import json
import os

from scrapy.crawler import CrawlerProcess

PATH=f'{os.getcwd()}\\ScrapyNewsWebsite\\'
NAME='news_bbc'

class NewsBBCSpider(scrapy.Spider):
    name = NAME
    start_urls=[]

    with open(f'{PATH}json\\{name}.json','w') as file:
        pass
    
    with open(f'{PATH}json\\search.json', 'r') as url_list:
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


def start(name):
    process = CrawlerProcess(settings={
        "FEEDS": {
            f'ScrapyNewsWebsite/json/{name}.json': {"format": "json", "overwrite": True},
        },
    })

    process.crawl(NewsBBCSpider)
    process.start()

start(NAME)