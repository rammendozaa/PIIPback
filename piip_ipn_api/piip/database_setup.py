from sqlalchemy.ext.declarative import declarative_base
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

base = declarative_base()

class PIIPModel(base):  # type: ignore
    __abstract__ = True
    __table_args__ = {"schema": "PIIP_pruebas"}


class DictActivityStatus(PIIPModel):
    __tablename__ = "DICT_ACTIVITY_STATUS"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)


class DictActivityType(PIIPModel):
    __tablename__ = "DICT_ACTIVITY_TYPE"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)


class DictInterviewType(PIIPModel):
    __tablename__ = "DICT_INTERVIEW_TYPE"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)


class DictCategory(PIIPModel):
    __tablename__ = "DICT_CATEGORY"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)


class DictCompany(PIIPModel):
    __tablename__ = "DICT_COMPANY"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)


class DictDifficulty(PIIPModel):
    __tablename__ = "DICT_DIFFICULTY"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)


class DictLanguage(PIIPModel):
    __tablename__ = "DICT_LANGUAGE"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)


class DictSchool(PIIPModel):
    __tablename__ = "DICT_SCHOOL"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)


class DictTrackingStatus(PIIPModel):
    __tablename__ = "DICT_TRACKING_STATUS"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)

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


class Administrator(PIIPModel):
    __tablename__ = "ADMINISTRATOR"

    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    password = Column(String(128), nullable=False)
    dob = Column(DateTime)
    first_name = Column(String(255))
    last_name = Column(String(255))
    is_super = Column(Boolean, DefaultClause("0"), nullable=False)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))



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


class Interview(PIIPModel):
    __tablename__ = "INTERVIEW"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    administrator_id = Column(Integer, ForeignKey(Administrator.id))
    language_id = Column(Integer, ForeignKey(DictLanguage.id))
    chosen_date = Column(DateTime)
    interview_url = Column(Text)
    interview_code = Column(Text)
    feedback = Column(Text)

    user = relationship("User", foreign_keys=[user_id])
    administrator = relationship("Administrator", foreign_keys=[administrator_id])
    language = relationship("DictLanguage", foreign_keys=[language_id])



class Problem(PIIPModel):
    __tablename__ = "PROBLEM"

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    description = Column(Text)
    test_cases = Column(Text)
    category_id = Column(Integer, ForeignKey(DictCategory.id))
    difficulty_id = Column(Integer, ForeignKey(DictDifficulty.id))
    url = Column(Text)
    time_limit = Column(Text)
    memory_limit = Column(Text)
    input = Column(Text)
    output = Column(Text)
    notes = Column(Text)
    source = Column(Text)
    solution = Column(Text)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))

    category = relationship("DictCategory", foreign_keys=[category_id])
    difficulty = relationship("DictDifficulty", foreign_keys=[difficulty_id])


class ProgrammingTopic(PIIPModel):
    __tablename__ = "PROGRAMMING_TOPIC"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(Text)
    file_route = Column(Text)
    information = Column(Text)
    created_date = Column(DateTime, DefaultClause(func.now()))


class SoftSkillTopic(PIIPModel):
    __tablename__ = "SOFT_SKILL_TOPIC"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(Text)
    file_route = Column(Text)
    information = Column(Text)
    created_date = Column(DateTime, DefaultClause(func.now()))


class SoftSkillQuestion(PIIPModel):
    __tablename__ = "SOFT_SKILL_QUESTION"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    question = Column(Text)
    file_route = Column(Text)
    information = Column(Text)
    created_date = Column(DateTime, DefaultClause(func.now()))


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



class CompanyTracking(PIIPModel):
    __tablename__ = "COMPANY_TRACKING"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    company_id = Column(Integer, ForeignKey(DictCompany.id), nullable=False)
    status_id = Column(Integer,  ForeignKey(DictTrackingStatus.id), nullable=False)
    application_url = Column(String(255))
    interview_date = Column(DateTime)

    user = relationship("User", foreign_keys=[user_id])
    company = relationship("DictCompany", foreign_keys=[company_id])
    status = relationship("DictTrackingStatus", foreign_keys=[status_id])


class CompanyTrackingLinks(PIIPModel):
    __tablename__ = "COMPANY_TRACKING_LINKS"

    id = Column(Integer, primary_key=True)
    company_tracking_id = Column(Integer, ForeignKey(CompanyTracking.id), nullable=False)
    description = Column(String(255), nullable=False)
    url = Column(String(1000), nullable=False)

    company_tracking = relationship("CompanyTracking", foreign_keys=[company_tracking_id])


class Template(PIIPModel):
    __tablename__ = "TEMPLATE"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(Text)
    position = Column(Integer)


class TemplateActivity(PIIPModel):
    __tablename__ = "TEMPLATE_ACTIVITY"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(Text)
    template_id = Column(Integer, ForeignKey(Template.id))
    activity_type_id = Column(Integer, ForeignKey(DictActivityType.id))
    position = Column(Integer)
    external_reference = Column(Integer)

    template = relationship("Template", foreign_keys=[template_id])
    activity = relationship("DictActivity", foreign_keys=[activity_type_id])


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
