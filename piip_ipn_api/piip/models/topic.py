from piip.models.database_setup import PIIPModel
from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    DefaultClause,
    String,
    DateTime,
    Text,
)
from sqlalchemy.sql import func


class ProgrammingTopic(PIIPModel):
    __tablename__ = "PROGRAMMING_TOPIC"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(Text)
    file_route = Column(Text)
    information = Column(Text)
    created_date = Column(DateTime, DefaultClause(func.now()))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)


class SoftSkillTopic(PIIPModel):
    __tablename__ = "SOFT_SKILL_TOPIC"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(Text)
    file_route = Column(Text)
    information = Column(Text)
    created_date = Column(DateTime, DefaultClause(func.now()))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
