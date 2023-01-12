from typing import List

from sqlalchemy import (BLOB, Boolean, Column, DateTime, DefaultClause,
                        ForeignKey, Integer, Numeric, String, Text)
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import RelationshipProperty
from sqlalchemy.sql import func

from piip.constants import DATABASE
from piip.models.database_setup import PIIPModel


class User(PIIPModel):
    __tablename__ = "USER"

    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    dob = Column(DateTime)
    salt = Column(BLOB)
    hash = Column(BLOB)
    first_name = Column(String(255))
    last_name = Column(String(255))
    school_id = Column(Integer, ForeignKey(f"{DATABASE}.DICT_SCHOOL.id"))
    is_active = Column(Integer, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))

    school = relationship("DictSchool", foreign_keys=[school_id])


class UserAdministrator(PIIPModel):
    __tablename__ = "USER_ADMINISTRATOR"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(f"{DATABASE}.USER.id"))
    administrator_id = Column(Integer, ForeignKey(f"{DATABASE}.ADMINISTRATOR.id"))
    is_graduate = Column(Boolean, DefaultClause("0"), nullable=False)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))

    user = relationship("User", foreign_keys=[user_id])
    administrator = relationship("Administrator", foreign_keys=[administrator_id])


class UserProblem(PIIPModel):
    __tablename__ = "USER_PROBLEM"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(f"{DATABASE}.USER.id"))
    problem_id = Column(Integer, ForeignKey(f"{DATABASE}.PROBLEM.id"))
    status_id = Column(
        Integer, DefaultClause("1"), ForeignKey(f"{DATABASE}.DICT_ACTIVITY_STATUS.id")
    )
    code = Column(Text)
    submission_url = Column(Text)
    language_id = Column(Integer, ForeignKey(f"{DATABASE}.DICT_LANGUAGE.id"))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))
    finished_date = Column(DateTime)

    user = relationship("User", foreign_keys=[user_id])
    problem = relationship("Problem", foreign_keys=[problem_id])
    status = relationship("DictActivityStatus", foreign_keys=[status_id])
    language = relationship("DictLanguage", foreign_keys=[language_id])


class UserProgrammingTopic(PIIPModel):
    __tablename__ = "USER_PROGRAMMING_TOPIC"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(f"{DATABASE}.USER.id"))
    programming_topic_id = Column(
        Integer, ForeignKey(f"{DATABASE}.PROGRAMMING_TOPIC.id")
    )
    status_id = Column(
        Integer, DefaultClause("1"), ForeignKey(f"{DATABASE}.DICT_ACTIVITY_STATUS.id")
    )
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))
    finished_date = Column(DateTime)

    user = relationship("User", foreign_keys=[user_id])
    programming_topic = relationship(
        "ProgrammingTopic", foreign_keys=[programming_topic_id]
    )
    status = relationship("DictActivityStatus", foreign_keys=[status_id])


class UserSoftSkillQuestion(PIIPModel):
    __tablename__ = "USER_SOFT_SKILL_QUESTION"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey(f"{DATABASE}.SOFT_SKILL_QUESTION.id"))
    user_id = Column(Integer, ForeignKey(f"{DATABASE}.USER.id"))
    status_id = Column(
        Integer, DefaultClause("1"), ForeignKey(f"{DATABASE}.DICT_ACTIVITY_STATUS.id")
    )
    answer = Column(Text)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))
    finished_date = Column(DateTime)

    question = relationship("SoftSkillQuestion", foreign_keys=[question_id])
    user = relationship("User", foreign_keys=[user_id])
    status = relationship("DictActivityStatus", foreign_keys=[status_id])


class UserSoftSkillTopic(PIIPModel):
    __tablename__ = "USER_SOFT_SKILL_TOPIC"

    id = Column(Integer, primary_key=True)
    soft_skill_topic_id = Column(Integer, ForeignKey(f"{DATABASE}.SOFT_SKILL_TOPIC.id"))
    user_id = Column(Integer, ForeignKey(f"{DATABASE}.USER.id"))
    status_id = Column(
        Integer, DefaultClause("1"), ForeignKey(f"{DATABASE}.DICT_ACTIVITY_STATUS.id")
    )
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))
    finished_date = Column(DateTime)

    soft_skill_topic = relationship(
        "SoftSkillTopic", foreign_keys=[soft_skill_topic_id]
    )
    user = relationship("User", foreign_keys=[user_id])
    status = relationship("DictActivityStatus", foreign_keys=[status_id])


class UserQuestionnaire(PIIPModel):
    __tablename__ = "USER_QUESTIONNAIRE"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(f"{DATABASE}.USER.id"))
    questionnaire_id = Column(Integer, ForeignKey(f"{DATABASE}.QUESTIONNAIRE.id"))
    correct_answers = Column(Integer)
    percentage_score = Column(Numeric(5, 2))
    answers = Column(Text)
    status_id = Column(
        Integer, DefaultClause("1"), ForeignKey(f"{DATABASE}.DICT_ACTIVITY_STATUS.id")
    )
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))
    finished_date = Column(DateTime)

    user = relationship("User", foreign_keys=[user_id])
    questionnaire = relationship("Questionnaire", foreign_keys=[questionnaire_id])


class UserTemplateActivity(PIIPModel):
    __tablename__ = "USER_TEMPLATE_ACTIVITY"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(f"{DATABASE}.USER.id"))
    template_activity_id = Column(
        Integer, ForeignKey(f"{DATABASE}.TEMPLATE_ACTIVITY.id")
    )
    status_id = Column(
        Integer, DefaultClause("1"), ForeignKey(f"{DATABASE}.DICT_ACTIVITY_STATUS.id")
    )
    user_template_section_id = Column(
        Integer, ForeignKey(f"{DATABASE}.USER_TEMPLATE_SECTION.id")
    )
    external_reference = Column(Integer)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))
    finished_date = Column(DateTime)
    position = Column(Integer)

    user_template_section = relationship(
        "UserTemplateSection",
        foreign_keys=[user_template_section_id],
        back_populates="user_activities",
    )
    user = relationship("User", foreign_keys=[user_id])
    template_activity = relationship(
        "TemplateActivity", foreign_keys=[template_activity_id]
    )
    status = relationship("DictActivityStatus", foreign_keys=[status_id])


class UserTemplateSection(PIIPModel):
    __tablename__ = "USER_TEMPLATE_SECTION"

    id = Column(Integer, primary_key=True)
    template_section_id = Column(Integer, ForeignKey(f"{DATABASE}.TEMPLATE_SECTION.id"))
    user_id = Column(Integer, ForeignKey(f"{DATABASE}.USER.id"))
    user_template_id = Column(Integer, ForeignKey(f"{DATABASE}.USER_TEMPLATE.id"))
    status_id = Column(
        Integer, DefaultClause("1"), ForeignKey(f"{DATABASE}.DICT_ACTIVITY_STATUS.id")
    )
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))
    position = Column(Integer)

    user_template = relationship(
        "UserTemplate", foreign_keys=[user_template_id], back_populates="user_sections"
    )
    template_section = relationship(
        "TemplateSection", foreign_keys=[template_section_id]
    )
    user = relationship("User", foreign_keys=[user_id])
    status = relationship("DictActivityStatus", foreign_keys=[status_id])
    user_activities: "RelationshipProperty[List[UserTemplateActivity]]" = relationship(
        "UserTemplateActivity", back_populates="user_template_section", lazy="dynamic"
    )


class UserTemplate(PIIPModel):
    __tablename__ = "USER_TEMPLATE"

    id = Column(Integer, primary_key=True)
    template_id = Column(Integer, ForeignKey(f"{DATABASE}.TEMPLATE.id"))
    user_id = Column(Integer, ForeignKey(f"{DATABASE}.USER.id"))
    status_id = Column(
        Integer, DefaultClause("1"), ForeignKey(f"{DATABASE}.DICT_ACTIVITY_STATUS.id")
    )
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))
    position = Column(Integer)

    template = relationship("Template", foreign_keys=[template_id])
    user = relationship("User", foreign_keys=[user_id])
    status = relationship("DictActivityStatus", foreign_keys=[status_id])
    user_sections: "RelationshipProperty[List[UserTemplateSection]]" = relationship(
        "UserTemplateSection", back_populates="user_template", lazy="dynamic"
    )
