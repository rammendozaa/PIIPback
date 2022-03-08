from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Boolean, 
    Column, 
    DateTime, 
    DefaultClause, 
    ForeignKey, 
    Integer, 
    String,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

base = declarative_base()

class PIIPModel(base):  # type: ignore
    __abstract__ = True
    __table_args__ = {"schema": "PIIP_pruebas"}
