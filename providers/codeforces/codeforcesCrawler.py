import scrapy
from scrapy.crawler import CrawlerProcess


class CodeforcesSpider(scrapy.Spider):
    name = "codeforces"
    start_urls = [
        'https://codeforces.com/problemset/problem/1625/C'
    ]
    def parse(self, response):
        page = response.url
        title = response.css('.title::text').get()
        timelimit = response.css('.time-limit::text').get()
        memoryLimit = response.css('.memory-limit::text').get()
        description = response.css('.problem-statement').xpath('div')[1].get()
        input = response.css('.input-specification').get()
        output = response.css('.output-specification').get()
        samples = response.css('.sample-tests').get()
        notes = response.css('.note').get()
        source = response.css('.rtable a').get()

process = CrawlerProcess()
process.crawl(CodeforcesSpider)
process.start()
