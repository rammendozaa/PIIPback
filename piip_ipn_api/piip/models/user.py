from piip.database_setup import PIIPModel
from piip.models import (
    Template, 
    TemplateActivity, 
    SoftSkillTopic, 
    ProgrammingTopic, 
    SoftSkillQuestion, 
    DictSchool, 
    Problem, 
    Administrator, 
    DictActivityStatus, 
    DictLanguage,
)

from sqlalchemy import (
    Boolean, 
    Column, 
    DateTime, 
    DefaultClause, 
    ForeignKey, 
    Integer, 
    String,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class User(PIIPModel):
    __tablename__ = "USER"
    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    password = Column(String(128))
    dob = Column(DateTime)
    first_name = Column(String(255))
    last_name = Column(String(255))
    school_id = Column(Integer, ForeignKey(DictSchool.id))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))

    school = relationship("DictSchool", foreign_keys=[school_id])

class UserAdministrator(PIIPModel):
    __tablename__ = "USER_ADMINISTRATOR"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    administrator_id = Column(Integer, ForeignKey(Administrator.id))
    is_graduate = Column(Boolean, DefaultClause("0"), nullable=False)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))

    user = relationship("User", foreign_keys=[user_id])
    administrator = relationship("Administrator", foreign_keys=[administrator_id])


class UserProblem(PIIPModel):
    __tablename__ = "USER_PROBLEM"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    problem_id = Column(Integer, ForeignKey(Problem.id))
    status_id = Column(Integer, ForeignKey(DictActivityStatus.id))
    code = Column(Text)
    language_id = Column(Integer, ForeignKey(DictLanguage.id))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))

    user = relationship("User", foreign_keys=[user_id])
    problem = relationship("Problem", foreign_keys=[problem_id])
    status = relationship("DictActivityStatus", foreign_keys=[status_id])
    language = relationship("DictLanguage", foreign_keys=[language_id])


class UserProgrammingTopic(PIIPModel):
    __tablename__ = "USER_PROGRAMMING_TOPIC"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    programming_topic_id = Column(Integer, ForeignKey(ProgrammingTopic.id))
    status_id = Column(Integer, ForeignKey(DictActivityStatus.id))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))

    user = relationship("User", foreign_keys=[user_id])
    programming_topic = relationship("ProgrammingTopic", foreign_keys=[programming_topic_id])
    status = relationship("DictActivityStatus", foreign_keys=[status_id])


class UserSoftSkillQuestion(PIIPModel):
    __tablename__ = "USER_SOFT_SKILL_QUESTION"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey(SoftSkillQuestion.id))
    user_id = Column(Integer, ForeignKey(User.id))
    status_id = Column(Integer, ForeignKey(DictActivityStatus.id))
    answer = Column(Text)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))

    question = relationship("SoftSkillQuestion", foreign_keys=[question_id])
    user = relationship("User", foreign_keys=[user_id])
    status = relationship("DictActivityStatus", foreign_keys=[status_id])


class UserSoftSkillTopic(PIIPModel):
    __tablename__ = "USER_SOFT_SKILL_TOPIC"

    id = Column(Integer, primary_key=True)
    soft_skill_topic_id = Column(Integer, ForeignKey(SoftSkillTopic.id))
    user_id = Column(Integer, ForeignKey(User.id))
    status_id = Column(Integer, ForeignKey(DictActivityStatus.id))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))

    soft_skill_topic = relationship("SoftSkillTopic", foreign_keys=True)
    user = relationship("User", foreign_keys=[user_id])
    status = relationship("DictActivityStatus", foreign_keys=[status_id])


class UserTemplate(PIIPModel):
    __tablename__ = "USER_TEMPLATE"

    id = Column(Integer, primary_key=True)
    template_id = Column(Integer, ForeignKey(Template.id))
    user_id = Column(Integer, ForeignKey(User.id))
    status_id = Column(Integer, ForeignKey(DictActivityStatus.id))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))

    template = relationship("Template", foreign_keys=[template_id])
    user = relationship("User", foreign_keys=[user_id])
    status = relationship("DictActivityStatus", foreign_keys=[status_id])


class UserTemplateActivity(PIIPModel):
    __tablename__ = "USER_TEMPLATE_ACTIVITY"

    id = Column(Integer, primary_key=True)
    template_activity_id = Column(Integer, ForeignKey(TemplateActivity.id))
    status_id = Column(Integer, ForeignKey(DictActivityStatus.id))
    external_reference = Column(Integer)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))

    template_activity = relationship("TemplateActivity", foreign_keys=[template_activity_id])
    status = relationship("DictActivityStatus", foreign_keys=[status_id])
