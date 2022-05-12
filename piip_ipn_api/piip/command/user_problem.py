from sqlalchemy import null
from piip.models import UserProblem
from piip.services.database.setup import session

def getNumberOfProblemsSolved(_user_id):
    numberOfProblems = session.query(UserProblem).filter_by(user_id=_user_id, status_id=4).count()
    return numberOfProblems

def updateProblemStatus(_user_id,_problem_id,status):
    statusID = 2
    if status == "AC":
        statusID = 4
    userProblem = session.query(UserProblem).filter_by(user_id=_user_id,problem_id=_problem_id).first()
    if userProblem:
        userProblem.status_id = statusID
        session.commit()
    else:
        userProblem = UserProblem(user_id = _user_id, problem_id= _problem_id,status_id = statusID)
        session.add(userProblem)
        session.commit()
