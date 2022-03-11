from sqlalchemy import null
from piip.models import Problem
from piip.services.database.setup import session
from piip.query.problem import get_problem_by_url
import re


def is_valid_problem(parse_response):
    problem = get_problem_by_url(parse_response.url)
    return (
        not problem
        and parse_response.url is not None
        and parse_response.css('.title::text').get() is not None
        and parse_response.css('.time-limit::text').get() is not None
        and parse_response.css('.memory-limit::text').get() is not None
        and parse_response.css('.problem-statement').xpath('div')[1].get() is not None
        and parse_response.css('.input-specification').get() is not None
        and parse_response.css('.output-specification').get() is not None
        and parse_response.css('.sample-tests').get() is not None
        and parse_response.css('.note').get() is not None
        and parse_response.css('.rtable a').get() is not None
    )


def add_problem_to_database(response, url):
    problemNum = getProblemNum(url)
    title = getValue("<div class=\"title\">\\s*"+problemNum+"\\. ([\\s\\S]*?)</div>",response.text)
    timelimit = getValue("</div>([\\d\\.]+) seconds?\\s*</div>", response.text)
    memorylimit = getValue("</div>(\\d+) megabytes\\s*</div>", response.text)
    description = getValue("standard output\\s*</div></div><div>([\\s\\S]*?)</div><div class=\"input-specification", response.text)
    input = getValue("<div class=\"section-title\">\\s*Input\\s*</div>([\\s\\S]*?)</div><div class=\"output-specification\">", response.text)
    output = getValue("<div class=\"section-title\">\\s*Output\\s*</div>([\\s\\S]*?)</div><div class=\"sample-tests\">", response.text)
    sampleInput = "<style type=\"text/css\">.input, .output {border: 1px solid #888888;} .output {margin-bottom:1em;position:relative;top:-1px;} .output pre,.input pre {background-color:#EFEFEF;line-height:1.25em;margin:0;padding:0.25em;} .title {background-color:#FFFFFF;border-bottom: 1px solid #888888;font-family:arial;font-weight:bold;padding:0.25em;}</style>"
    sampleInput += getValue("<div class=\"sample-test\">([\\s\\S]*?)</div>\\s*</div>\\s*</div>", response.text)
    hint = getValue("<div class=\"section-title\">\\s*Note\\s*</div>([\\s\\S]*?)</div></div></div></div>", response.text)
    source = getValue("(<a[^<>]+/contest/\\d+\">.+?</a>)",response.text)

    problem = Problem(
        title = title,
        description = description,
        test_cases = sampleInput,
        category_id = 1,
        difficulty_id = 1,
        url = url,
        time_limit = timelimit,
        memory_limit = memorylimit,
        input = input,
        output = output,
        notes = hint,
        source = source,
        solution = "There is no solution"
    )
    session.add(problem)
    session.commit()


def get_all_problems():
    return session.query(Problem).all()

def getProblem(_problem_id):
    problem = session.query(Problem).filter_by(id=_problem_id).first()
    if not problem:
        return null
    return problem

def getProblemCode(problem_url):
    cnt = 0
    problem_code = ""
    for c in problem_url[::-1]:
        if cnt == 2:
            break
        if c == '/':
            cnt += 1
        else:
            problem_code += c
    return problem_code[::-1]

def getProblemNum(url):
    problemNum = ""
    for c in url[::-1]:
        if c == '/':
            break
        problemNum += c
    return problemNum[::-1]

def getValue(pattern, text):
    res = re.findall(pattern, text)
    if len(res) == 0:
        return ""
    return res[0]