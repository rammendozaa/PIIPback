from sqlalchemy import (Boolean, Column, DateTime, DefaultClause, Integer,
                        String, Text)
from sqlalchemy.sql import func

from piip.models.database_setup import PIIPModel


class ProgrammingTopic(PIIPModel):
    __tablename__ = "PROGRAMMING_TOPIC"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(Text)
    topic_information = Column(Text)
    created_date = Column(DateTime, DefaultClause(func.now()))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_by = Column(Integer)


class SoftSkillTopic(PIIPModel):
    __tablename__ = "SOFT_SKILL_TOPIC"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(Text)
    topic_information = Column(Text)
    created_date = Column(DateTime, DefaultClause(func.now()))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_by = Column(Integer)
