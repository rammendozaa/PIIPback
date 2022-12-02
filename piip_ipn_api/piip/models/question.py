from sqlalchemy import (Boolean, Column, DateTime, DefaultClause, Integer,
                        String, Text)
from sqlalchemy.sql import func

from piip.models.database_setup import PIIPModel


class SoftSkillQuestion(PIIPModel):
    __tablename__ = "SOFT_SKILL_QUESTION"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    question = Column(Text)
    created_date = Column(DateTime, DefaultClause(func.now()))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_by = Column(Integer)
