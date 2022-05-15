from asyncio import current_task
from curses.ascii import NUL
from sqlalchemy import null
from piip.models import UserProblem
from piip.services.database.setup import session
from piip.command.problem import getProblem
from datetime import date

def getNumberOfProblemsSolvedByDay(_user_id):
    problemsSolved = session.query(UserProblem).filter_by(user_id=_user_id, status_id=4)
    cntByDay = {}
    for user_problem in problemsSolved:
        day = user_problem.finished_date
        if day is None:
            continue
        formattedDay = day.strftime("%B %d, %Y")
        if day in cntByDay:
            cntByDay[formattedDay] += 1
        else: 
            cntByDay[formattedDay] = 1

    return cntByDay

def getNumberOfProblemsSolvedByTag(_user_id):
    problemsSolved = session.query(UserProblem).filter_by(user_id=_user_id, status_id=4)
    cntByTag = {}
    for user_problem in problemsSolved:
        problemId = user_problem.problem_id
        problem = getProblem(problemId)
        
        currentTag = ""
        for c in problem.tags:
            if c == '_':
                if currentTag in cntByTag:
                    cntByTag[currentTag] += 1
                else: 
                    cntByTag[currentTag] = 1
                currentTag = ""
            else:
                currentTag += c
        if len(currentTag) > 0:
            if currentTag in cntByTag:
                cntByTag[currentTag] += 1
            else: 
                cntByTag[currentTag] = 1
    return cntByTag

def getNumberOfProblemsSolved(_user_id):
    numberOfProblems = session.query(UserProblem).filter_by(user_id=_user_id, status_id=4).count()
    return numberOfProblems

def updateProblemStatus(_user_id,_problem_id,status):
    statusID = 2
    finishedDate = date.today().strftime('%Y-%m-%d %H:%M:%S')
    if status == "AC":
        statusID = 4
    userProblem = session.query(UserProblem).filter_by(user_id=_user_id,problem_id=_problem_id).first()
    if userProblem:
        userProblem.status_id = statusID
        if statusID == 4:
            userProblem.finished_date = finishedDate
        session.commit()
    else:
        if statusID == 4:
            userProblem = UserProblem(user_id = _user_id, problem_id= _problem_id,status_id = statusID, finished_date = finishedDate)
        else:
            userProblem = UserProblem(user_id = _user_id, problem_id= _problem_id,status_id = statusID)
        session.add(userProblem)
        session.commit()
