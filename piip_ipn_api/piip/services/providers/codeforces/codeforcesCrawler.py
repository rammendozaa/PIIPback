import requests

from piip.command.problem import add_problem_to_database


class CodeforcesSpider:
    name = "codeforces"

    def start(self):
        urls = self.getUrls(20)
        for url in urls:
            session = requests.session()
            response = session.get(url)
            add_problem_to_database(response, url)
            with open("hola.html", "wb") as f:
                f.write(response.text.encode())

    def getUrls(self, noProblems):
        r = requests.get("https://codeforces.com/api/problemset.problems")
        problems = r.json()["result"]["problems"]
        urls = []
        for problem in problems:
            if noProblems == 0:
                break
            url = "https://codeforces.com/problemset/problem/%s/%s" % (
                problem["contestId"],
                problem["index"],
            )
            urls.append(url)
            noProblems -= 1
        return urls
