from sqlalchemy import desc
from piip.command.problem import add_problem_to_database
import requests


class CodeforcesSpider():
    name = "codeforces"
    def start(self):
        urls = self.getUrls(10)
        for url in urls:
            session = requests.session()
            headers = {'Cookie': '__utma=71512449.29827362.1651451496.1651451496.1651451496.1; __utmb=71512449.7.10.1651451496; __utmc=71512449; __utmz=71512449.1651451496.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; 39ce7=CFuEwK5j; JSESSIONID=3BE310C89FF9E4A26D3D42246433B830-n1; RCPC=321e98c6924c9099eff2879a4f165737'}
            response = session.get(url, headers=headers)
            add_problem_to_database(response,url)
            '''
            with open('hola.html','wb') as f:
                f.write(response.text.encode())
            '''
    def getUrls(self, noProblems):
        r = requests.get('https://codeforces.com/api/problemset.problems')
        problems = r.json()["result"]["problems"]
        urls = []
        for problem in problems:
            if noProblems == 0:
                break
            url = "https://codeforces.com/problemset/problem/%s/%s" % (problem["contestId"],problem["index"])
            urls.append(url)
            noProblems -= 1
        return urls
