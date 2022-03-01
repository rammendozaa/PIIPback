from piip.database_setup import PIIPModel
from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    DefaultClause,
    String,
    DateTime,
)
from sqlalchemy.sql import func

class Administrator(PIIPModel):
    __tablename__ = "ADMINISTRATOR"

    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    password = Column(String(128), nullable=False)
    dob = Column(DateTime)
    first_name = Column(String(255))
    last_name = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))

"""
class AdministratorBehavioralQuestion(PIIPModel):
    __tablename__ = "ADMINISTRATOR_BEHAVIORAL_QUESTION"


class AdministratorProblem(PIIPModel):
    __tablename__ = "ADMINISTRATOR_PROBLEM"


class AdministratorProgrammingTopic(PIIPModel):
    __tablename__ = "ADMINISTRATOR_PROGRAMMING_TOPIC"


class AdministratorSoftSkillTopic(PIIPModel):
    __tablename__ = "ADMINISTRATOR_SOFT_SKILL_TOPIC"
"""