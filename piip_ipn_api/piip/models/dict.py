from piip.database_setup import PIIPModel

from sqlalchemy import Boolean, Column, DateTime, DefaultClause, ForeignKey, Integer, String

class DictSchool(PIIPModel):
    __tablename__ = "DICT_SCHOOL"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))


class DictAssignmentStatus(PIIPModel):
    __tablename__ = "DICT_ASSIGNMENT_STATUS"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))


class DictCategory(PIIPModel):
    __tablename__ = "DICT_CATEGORY"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))


class DictCompany(PIIPModel):
    __tablename__ = "DICT_COMPANY"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))


class DictDifficulty(PIIPModel):
    __tablename__ = "DICT_DIFFICULTY"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))


class DictInterviewStatus(PIIPModel):
    __tablename__ = "DICT_INTERVIEW_STATUS"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))


class DictLanguage(PIIPModel):
    __tablename__ = "DICT_LANGUAGE"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))


class DictTrackingStatus(PIIPModel):
    __tablename__ = "DICT_TRACKING_STATUS"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
