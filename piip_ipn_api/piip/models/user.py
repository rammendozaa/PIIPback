from piip.database_setup import PIIPModel

from sqlalchemy import (
    Boolean, 
    Column, 
    DateTime, 
    DefaultClause, 
    ForeignKey, 
    Integer, 
    String)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class User(PIIPModel):
    __tablename__ = "USER"

    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    password = Column(String(128))
    dob = Column(DateTime, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    school_id = Column(Integer, ForeignKey("DICT_SCHOOL.id"), nullable=False)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()),nullable=False)

    school = relationship("DictSchool", foreign_keys=[school_id])


class UserBehavioralQuestion(PIIPModel):
    __tablename__ = "USER_BEHAVIORAL_QUESTION"


class UserProblem(PIIPModel):
    __tablename__ = "USER_PROBLEM"