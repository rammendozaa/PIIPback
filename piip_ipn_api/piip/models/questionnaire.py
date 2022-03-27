from piip.models.database_setup import PIIPModel
from sqlalchemy import (
    Column,
    Integer,
    DefaultClause,
    DateTime,
    Text,
    String,
)
from sqlalchemy.sql import func


class Questionnaire(PIIPModel):
    __tablename__ = "QUESIONNAIRE"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    questions = Column(Text)
    questions_route = Column(Text)
    total_questions = Column(Integer)
    answers = Column(Text)
    created_date = Column(DateTime, DefaultClause(func.now()))
