from sqlalchemy import null
from piip.services.database.setup import session
from datetime import date
from piip.models import User,UserAdministrator
from piip.models.user import UserTemplateSection, UserTemplate, UserTemplateActivity
from piip.models.user import UserProblem, UserProgrammingTopic, UserQuestionnaire, UserSoftSkillQuestion, UserSoftSkillTopic
from piip.models.interview import Interview
from piip.query.template import get_template_by_id
from piip.query.user import (
    get_active_templates_by_user_id,
    get_user_template_by_id,
    get_user_template_section_by_id,
    get_user_template_activity_by_id,
)
from piip.command.constants import ACTIVITY_TYPES

def insertUser(_firstname, _lastname, _email, _school_id, _password):
    # Check if user already exits
    user = session.query(User).filter_by(email=_email).first()
    if user:
        return 0
    new_user = User(email=_email, password=_password, dob=date.today(), first_name=_firstname, last_name=_lastname, school_id=_school_id)
    session.add(new_user)
    session.commit()
    print(new_user.id)
    insertUserAdministrator(new_user)
    return 1

def insertUserAdministrator(user):
    user_administrator = UserAdministrator(user_id=user.id)
    session.add(user_administrator)
    session.commit()

def getAdministratorGivenUser(_email):
    user = session.query(User).filter_by(email=_email).first()
    _user_id = user.id
    administrator = session.query(UserAdministrator).filter_by(user_id=_user_id).first()
    if administrator.administrator_id == None:
        return -1
    return administrator.administrator_id

def getUnassignedUsers():
    users = session.query(UserAdministrator).filter_by(administrator_id=None).all()
    return users

def getMyStudents(_administrator_id):
    users = session.query(UserAdministrator).filter_by(administrator_id=_administrator_id).all()
    return users

def getUser(_email):
    user = session.query(User).filter_by(email=_email).first()
    return user


def create_user_problem(user_id, external_reference):
    user_problem = UserProblem(user_id=user_id,problem_id=external_reference)
    session.add(user_problem)
    session.commit()


def create_user_programming_topic(user_id, external_reference):
    user_programming_topic = UserProgrammingTopic(user_id=user_id, programming_topic_id=external_reference)
    session.add(user_programming_topic)
    session.commit()


def create_user_soft_skill_question(user_id, external_reference):
    user_soft_skill_question = UserSoftSkillQuestion(user_id=user_id, question_id=external_reference)
    session.add(user_soft_skill_question)
    session.commit()


def create_user_soft_skill_topic(user_id, external_reference):
    user_soft_skill_topic = UserSoftSkillTopic(user_id=user_id, soft_skill_topic_id=external_reference)
    session.add(user_soft_skill_topic)
    session.commit()


def create_user_interview(user_id, user_admin_id):
    user_interview = Interview(
        user_id=user_id,
        administrator_id=user_admin_id,
    )
    session.add(user_interview)
    session.commit()
    return user_interview


def create_user_questionnaire(user_id, external_reference):
    user_questionnaire = UserQuestionnaire(user_id=user_id, questionnaire_id=external_reference)
    session.add(user_questionnaire)
    session.commit()


def assign_template_activity_to_user_id(user_id, activity, user_template_section_id):
    activity_type = activity.activity_type_id
    user_template_activity = UserTemplateActivity(
        user_id=user_id,
        template_activity_id=activity.id,
        user_template_section_id=user_template_section_id,
        external_reference=activity.external_reference,
        position=activity.position,
    )
    session.add(user_template_activity)
    session.commit()
    if activity_type == ACTIVITY_TYPES["PROBLEM"]:
        create_user_problem(user_id, activity.external_reference)
    if activity_type == ACTIVITY_TYPES["PROGRAMMING_TOPIC"]:
        create_user_programming_topic(user_id, activity.external_reference)
    if activity_type == ACTIVITY_TYPES["SOFT_SKILL_QUESTION"]:
        create_user_soft_skill_question(user_id, activity.external_reference)
    if activity_type == ACTIVITY_TYPES["SOFT_SKILL_TOPIC"]:
        create_user_soft_skill_topic(user_id, activity.external_reference)
    if activity_type == ACTIVITY_TYPES["QUESTIONNAIRE"]:
        create_user_questionnaire(user_id, activity.external_reference)

    return user_template_activity


def assign_template_section_to_user_id(user_id, section, user_template_id):
    user_template_section = UserTemplateSection(
        template_section_id=section.id,
        user_template_id=user_template_id,
        user_id=user_id,
        position=section.position,
    )
    session.add(user_template_section)
    session.commit()
    for activity in section.activities:
        assign_template_activity_to_user_id(user_id, activity, user_template_section.id)
    return user_template_section


def assign_template_to_user_id(user_id, template_ids):
    count = 1
    templates = []
    for id in template_ids:
        template = get_template_by_id(id)
        user_template = UserTemplate(
            template_id=template.id,
            user_id=user_id,
            position=count,
        )
        count += 1
        session.add(user_template)
        session.commit()
        templates.append(user_template)
        for section in template.sections:
            assign_template_section_to_user_id(user_id, section, user_template.id)
    return templates


def get_active_user_templates(user_id):
    return get_active_templates_by_user_id(user_id)
    

def disable_user_template_by_id(user_template_id):
    template = get_user_template_by_id(user_template_id)
    if not template:
        raise "User template not found"
    template.is_active = False
    session.add(template)
    session.commit()
    return template


def disable_user_template_section_by_id(user_template_section_id):
    template_section = get_user_template_section_by_id(user_template_section_id)
    if not template_section:
        raise "User template section not found"
    template_section.user_template_id = None 
    template_section.is_active = False
    session.add(template_section)
    session.commit()
    return template_section


def disable_user_template_activity_by_id(user_template_activity_id):
    template_activity = get_user_template_activity_by_id(user_template_activity_id)
    if not template_activity:
        raise "User template activity not found"
    template_activity.user_template_section_id = None
    template_activity.is_active = False
    session.add(template_activity)
    session.commit()
    return template_activity
