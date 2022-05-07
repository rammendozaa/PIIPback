from sqlalchemy import null
from piip.models import UserProgrammingTopic
from piip.services.database.setup import session

def getNumberOfProgrammingTopicsSolved(_user_id):
    number = session.query(UserProgrammingTopic).filter_by(user_id=_user_id, status_id=4).count()
    return number