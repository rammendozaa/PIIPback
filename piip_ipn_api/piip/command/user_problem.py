from sqlalchemy import null
from piip.models import UserProblem
from piip.services.database.setup import session

def getNumberOfProblemsSolved(_user_id):
    numberOfProblems = session.query(UserProblem).filter_by(user_id=_user_id, status_id=4).count()
    return numberOfProblems