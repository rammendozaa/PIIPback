from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()

class PIIPModel(base):  # type: ignore
    __abstract__ = True
    __table_args__ = {"schema": "PIIP_pruebas"}
