from sqlalchemy import ForeignKey
from piip.models.database_setup import PIIPModel
from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    DefaultClause,
    DateTime,
    Text,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from piip.models.constants import DATABASE


class Problem(PIIPModel):
    __tablename__ = "PROBLEM"

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    description = Column(Text)
    test_cases = Column(Text)
    category_id = Column(Integer, ForeignKey(f"{DATABASE}.DICT_CATEGORY.id"))
    difficulty_id = Column(Integer, ForeignKey(f"{DATABASE}.DICT_DIFFICULTY.id"))
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
    finished_date = Column(DateTime)

    category = relationship("DictCategory", foreign_keys=[category_id])
    difficulty = relationship("DictDifficulty", foreign_keys=[difficulty_id])
