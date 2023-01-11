from dataclasses import dataclass
from typing import List

from sqlalchemy import (Boolean, Column, DateTime, DefaultClause, ForeignKey,
                        Integer, String, Text)
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import RelationshipProperty
from sqlalchemy.sql import func

from piip.constants import DATABASE
from piip.models.database_setup import PIIPModel


class QuestionnaireQuestion(PIIPModel):
    __tablename__ = "QUESTIONNAIRE_QUESTION"

    id = Column(Integer, primary_key=True)
    questionnaire_id = Column(Integer, ForeignKey(f"{DATABASE}.QUESTIONNAIRE.id"))
    question = Column(Text)
    answer = Column(Text)
    option_1 = Column(Text)
    option_2 = Column(Text)
    option_3 = Column(Text)
    created_date = Column(DateTime, DefaultClause(func.now()))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)

    questionnaire = relationship(
        "Questionnaire", foreign_keys=[questionnaire_id], back_populates="questions"
    )


class Questionnaire(PIIPModel):
    __tablename__ = "QUESTIONNAIRE"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(Text)
    total_questions = Column(Integer)
    created_date = Column(DateTime, DefaultClause(func.now()))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_by = Column(Integer)

    questions: "RelationshipProperty[List[QuestionnaireQuestion]]" = relationship(
        "QuestionnaireQuestion", back_populates="questionnaire", lazy="dynamic"
    )


@dataclass
class CreateQuestionnaire:
    title: str
    description: str
    questions: List[dict]
    created_by: int
