from sqlalchemy import (BLOB, Boolean, Column, DateTime, DefaultClause,
                        Integer, String)
from sqlalchemy.sql import func

from piip.models.database_setup import PIIPModel


class Administrator(PIIPModel):
    __tablename__ = "ADMINISTRATOR"

    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    dob = Column(DateTime)
    first_name = Column(String(255))
    last_name = Column(String(255))
    is_super = Column(Boolean, DefaultClause("0"), nullable=False)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))
    salt = Column(BLOB)
    hash = Column(BLOB)
