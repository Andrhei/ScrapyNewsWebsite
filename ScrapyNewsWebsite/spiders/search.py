import scrapy
import os

from scrapy.crawler import CrawlerProcess

PATH=f'{os.getcwd()}\\ScrapyNewsWebsite\\'
NAME='search'

class SearchSpider(scrapy.Spider):
    name=NAME
    start_urls=["https://www.bbc.com/news"]

    with open(f'{PATH}json\\{name}.json','w') as file:
        pass

    def parse(self, response, **kwargs):
        nav = response.css('nav.nw-c-nav__wide')
        li = nav.css('li')
        for element in li:
            url = str(element.css('a::attr(href)').get())
            yield {"url":f'https://www.bbc.com{url}'}
    

def start(name):
    process = CrawlerProcess(settings={
        "FEEDS": {
            f'ScrapyNewsWebsite/json/{name}.json': {"format": "json", "overwrite": True},
        },
    })

    process.crawl(SearchSpider)
    process.start()

start(NAME)