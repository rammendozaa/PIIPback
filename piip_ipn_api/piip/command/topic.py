from piip.models import ProgrammingTopic, SoftSkillTopic
from piip.services.database.setup import session

def get_all_programming_topics():
    return session.query(ProgrammingTopic).all()

def get_all_softskills_topics():
    return session.query(SoftSkillTopic).all()

