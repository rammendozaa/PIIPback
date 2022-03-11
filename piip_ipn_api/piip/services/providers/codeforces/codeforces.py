import re
import requests
import random

#https://gist.github.com/551100kk/68e42969cc58fc75e24d3613c5c8c601
class Codeforces:
    def __init__(self):
        self.session = requests.session()
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
        }

    def login(self, username, password):
        self.username = username
        url = 'https://codeforces.com/enter'
        result = self.session.get(url, headers=self.headers)
        csrf_token_pattern = r'name=["\']csrf_token["\'] value=["\'](.*?)["\']'
        ftaa_pattern = r'window._ftaa = ["\'](.*?)["\']'
        bfaa_pattern = r'window._bfaa = ["\'](.*?)["\']'
        data = {
            'csrf_token': re.findall(csrf_token_pattern, result.text)[0],
            'action': 'enter',
            'ftaa': re.findall(ftaa_pattern, result.text)[0],
            'bfaa': re.findall(bfaa_pattern, result.text)[0],
            'handleOrEmail': username,
            'password': password,
            '_tta': 487,
        }
        login_result = self.session.post(url, data=data, headers=self.headers)

    def check_login(self):
        url = 'https://codeforces.com'
        result = self.session.get(url, headers=self.headers)
        if self.username in result.text:
            print('Success!')
            return True
        
        print('Login failed!')
        return False

    def submit(self, problem, code):
        url = 'https://codeforces.com/problemset/submit'
        result = self.session.get(url, headers=self.headers)
        csrf_token_pattern = r'name=["\']csrf_token["\'] value=["\'](.*?)["\']'
        ftaa_pattern = r'window._ftaa = ["\'](.*?)["\']'
        bfaa_pattern = r'window._bfaa = ["\'](.*?)["\']'
        data = {
            'csrf_token': re.findall(csrf_token_pattern, result.text)[0],
            'action': 'submitSolutionFormSubmitted',
            'ftaa': re.findall(ftaa_pattern, result.text)[0],
            'bfaa': re.findall(bfaa_pattern, result.text)[0],
            'submittedProblemCode': problem,
            'programTypeId': 54,
            'source': '', 
            'tabSize': 4,
            'sourceFile': code, 
            '_tta': 377,
        }
        url = 'https://codeforces.com/problemset/submit?csrf_token=' + re.findall(csrf_token_pattern, result.text)[0]
        result2 = self.session.post(url, data=data, headers=self.headers)
        return "result2"
        #submission_id_pattern = r'href="\/problemset\/submission\/(.*?)"'
        #submissionUrl = "https://codeforces.com/problemset/submission/"+re.findall(submission_id_pattern,result2.text)[0]
        #eturn submissionUrl

    def getSubmissionStatus(self, submissionUrl):
        result = self.session.get(submissionUrl, headers=self.headers)
        if 'verdict-waiting' in result.text:
            return {"verdict":"Running ..."}
        elif 'verdict-accepted' in result.text:
            return {"verdict":"AC"}
        elif 'verdict-rejected' in result.text:
            return {"verdict":"WA"}
        else:
            return {"verdict":"CE"}

#if __name__ == '__main__':
#    codeforces = Codeforces()
#    codeforces.login('Barbosa1998', 'Barbosa20111910')
#    if codeforces.check_login():
#        codeforces.submit('1254A', 'qwer' + str(random.random()))
