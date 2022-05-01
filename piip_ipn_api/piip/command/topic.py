from piip.models import ProgrammingTopic, SoftSkillTopic
from piip.services.database.setup import session

def get_all_programming_topics():
    return session.query(ProgrammingTopic).all()


def get_all_softskills_topics():
    return session.query(SoftSkillTopic).all()


def create_soft_skill_topic(soft_skill_topic_to_add):
    session.add(soft_skill_topic_to_add)
    session.commit()
    return soft_skill_topic_to_add


def create_algorithm_topic(algorithm_topic_to_add):
    session.add(algorithm_topic_to_add)
    session.commit()
    return algorithm_topic_to_add
