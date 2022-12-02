
from piip.models import UserSoftSkillTopic
from piip.services.database.setup import session


def getNumberOfSoftSkillTopicsSolved(_user_id):
    number = (
        session.query(UserSoftSkillTopic)
        .filter_by(user_id=_user_id, status_id=4)
        .count()
    )
    return number
