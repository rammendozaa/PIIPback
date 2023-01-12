from sqlalchemy.ext.declarative import declarative_base

from piip.constants import DATABASE

base = declarative_base()


class PIIPModel(base):  # type: ignore
    __abstract__ = True
    __table_args__ = {"schema": DATABASE}
