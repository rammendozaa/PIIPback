from sqlalchemy import (Boolean, Column, DateTime, DefaultClause, ForeignKey,
                        Integer, Text)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from piip.models.constants import DATABASE
from piip.models.database_setup import PIIPModel


class Problem(PIIPModel):
    __tablename__ = "PROBLEM"

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    description = Column(Text)
    test_cases = Column(Text)
    tags = Column(Text)
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

    difficulty = relationship("DictDifficulty", foreign_keys=[difficulty_id])
