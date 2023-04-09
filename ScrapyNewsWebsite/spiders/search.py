import scrapy

from scrapy.crawler import CrawlerProcess

class SearchSpider(scrapy.Spider):
    name="search"
    start_urls=["https://www.bbc.com/news"]

    with open(f'{name}.json','w') as file:
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
            f'{name}.json': {"format": "json"},
        },
    })

    process.crawl(SearchSpider)
    process.start()

start('search')