import scrapy

class SearchSpider(scrapy.Spider):
    name="search"
    start_urls=["https://www.bbc.com/news"]

    def parse(self, response, **kwargs):
        nav = response.css('nav.nw-c-nav__wide')
        li = nav.css('li')
        for element in li:
            url = str(element.css('a::attr(href)').get())
            yield {"url":f'https://www.bbc.com{url}'}
        

