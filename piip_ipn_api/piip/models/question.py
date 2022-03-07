from piip.database_setup import PIIPModel
from sqlalchemy import (
    Column,
    Integer,
    DefaultClause,
    String,
    DateTime,
    Text,
)
from sqlalchemy.sql import func


class SoftSkillQuestion(PIIPModel):
    __tablename__ = "SOFT_SKILL_QUESTION"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    question = Column(Text)
    file_route = Column(Text)
    information = Column(Text)
    created_date = Column(DateTime, DefaultClause(func.now()))
