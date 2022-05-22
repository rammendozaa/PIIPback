from piip.models import ProgrammingTopic, SoftSkillTopic
from piip.services.database.setup import session
from piip.models.user import (
    UserProgrammingTopic,
    UserSoftSkillTopic,
)

def get_all_programming_topics():
    return session.query(ProgrammingTopic).filter(ProgrammingTopic.is_active == True).all()


def get_programming_topic(topic_id):
    return session.query(ProgrammingTopic).get(topic_id)


def get_all_softskills_topics():
    return session.query(SoftSkillTopic).filter(SoftSkillTopic.is_active == True).all()


def get_softskill_topic(topic_id):
    return session.query(SoftSkillTopic).get(topic_id)


def create_soft_skill_topic(soft_skill_topic_to_add):
    session.add(soft_skill_topic_to_add)
    session.commit()
    return soft_skill_topic_to_add


def create_algorithm_topic(algorithm_topic_to_add):
    session.add(algorithm_topic_to_add)
    session.commit()
    return algorithm_topic_to_add


def get_all_unassigned_programming_topics(user_id):
    user_programming_topics = (
        session.query(UserProgrammingTopic.programming_topic_id)
        .filter(UserProgrammingTopic.user_id == user_id, UserProgrammingTopic.is_active == True)
        .all()
    )
    topic_list = [topics[0] for topics in user_programming_topics]
    return session.query(ProgrammingTopic).filter(ProgrammingTopic.id.notin_(topic_list)).all()


def get_all_unassigned_softskills_topics(user_id):
    user_softskills_topics = (
        session.query(UserSoftSkillTopic.soft_skill_topic_id)
        .filter(UserSoftSkillTopic.user_id == user_id, UserSoftSkillTopic.is_active == True)
        .all()
    )
    topic_list = [topics[0] for topics in user_softskills_topics]
    return session.query(SoftSkillTopic).filter(SoftSkillTopic.id.notin_(topic_list)).all()
