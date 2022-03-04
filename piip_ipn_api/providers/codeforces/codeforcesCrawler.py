import scrapy
from scrapy.crawler import CrawlerProcess
import requests


class CodeforcesSpider(scrapy.Spider):
    name = "codeforces"
    
    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.start_urls = self.urls

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


def getUrls():
    r = requests.get('https://codeforces.com/api/problemset.problems')
    problems = r.json()["result"]["problems"]
    urls = []
    for problem in problems:
        url = "https://codeforces.com/problemset/problem/%s/%s" % (problem["contestId"],problem["index"])
        urls.append(url)
    return urls

process = CrawlerProcess()
process.crawl(CodeforcesSpider, urls=getUrls())
process.start()
