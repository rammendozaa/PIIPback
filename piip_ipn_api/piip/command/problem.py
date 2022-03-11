from sqlalchemy import null
from piip.models import Problem
from piip.services.database.setup import session

def is_valid_problem(parse_response):
    return (
        parse_response.url is not None
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


def add_problem_to_database(parse_response):
    page = parse_response.url
    title = parse_response.css('.title::text').get()
    timelimit = parse_response.css('.time-limit::text').get()
    memoryLimit = parse_response.css('.memory-limit::text').get()
    description = parse_response.css('.problem-statement').xpath('div')[1].get()
    input = parse_response.css('.input-specification').get()
    output = parse_response.css('.output-specification').get()
    samples = parse_response.css('.sample-tests').get()
    notes = parse_response.css('.note').get()
    source = parse_response.css('.rtable a').get()

    if is_valid_problem(parse_response):
        problem = Problem(
            title = title,
            description = description,
            test_cases = samples,
            category_id = 1,
            difficulty_id = 1,
            url = page,
            time_limit = timelimit,
            memory_limit = memoryLimit,
            input = input,
            output = output,
            notes = notes,
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