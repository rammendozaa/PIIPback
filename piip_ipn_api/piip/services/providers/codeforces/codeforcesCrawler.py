import scrapy
import requests
from piip.command.problem import add_problem_to_database

class CodeforcesSpider(scrapy.Spider):
    name = "codeforces"
    
    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.start_urls = self.urls

    def parse(self, response):
        try:
            add_problem_to_database(response)
        except Exception as e:
            pass

def getUrls():
    r = requests.get('https://codeforces.com/api/problemset.problems')
    problems = r.json()["result"]["problems"]
    urls = []
    for problem in problems:
        url = "https://codeforces.com/problemset/problem/%s/%s" % (problem["contestId"],problem["index"])
        urls.append(url)
    return urls
