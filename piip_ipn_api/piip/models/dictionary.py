from sqlalchemy import Boolean, Column, DefaultClause, Integer, String

from piip.models.database_setup import PIIPModel


class DictActivityStatus(PIIPModel):
    __tablename__ = "DICT_ACTIVITY_STATUS"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)


class DictActivityType(PIIPModel):
    __tablename__ = "DICT_ACTIVITY_TYPE"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)


class DictInterviewType(PIIPModel):
    __tablename__ = "DICT_INTERVIEW_TYPE"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)


class DictCompany(PIIPModel):
    __tablename__ = "DICT_COMPANY"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)


class DictDifficulty(PIIPModel):
    __tablename__ = "DICT_DIFFICULTY"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)


class DictLanguage(PIIPModel):
    __tablename__ = "DICT_LANGUAGE"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)


class DictSchool(PIIPModel):
    __tablename__ = "DICT_SCHOOL"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)


class DictTrackingStatus(PIIPModel):
    __tablename__ = "DICT_TRACKING_STATUS"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
