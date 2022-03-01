from fileinput import filename
import scrapy


class PostsSpider(scrapy.Spider):
    name = "posts"
    start_urls = [
        'https://codeforces.com/problemset/problem/1625/E1',
        'https://codeforces.com/problemset/problem/1625/C',
    ]

    def parse(self, response):
        page = response.url
        filename = 'hola.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

# response.css('.title::text').get()
# response.css('.time-limit::text').get()
# response.css('.memory-limit::text').get()
# response.css('.problem-statement').xpath('div')[1].get()