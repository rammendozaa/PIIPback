from piip.models.database_setup import PIIPModel
from sqlalchemy import (
    Boolean,
    DefaultClause,
    Column, 
    DateTime, 
    ForeignKey, 
    Integer, 
    Text,
)
from sqlalchemy.orm import relationship
from piip.models.constants import DATABASE

class Interview(PIIPModel):
    __tablename__ = "INTERVIEW"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(f"{DATABASE}.USER.id"))
    administrator_id = Column(Integer, ForeignKey(f"{DATABASE}.ADMINISTRATOR.id"))
    language_id = Column(Integer, ForeignKey(f"{DATABASE}.DICT_LANGUAGE.id"))
    interview_type_id = Column(Integer, DefaultClause("1"), ForeignKey(f"{DATABASE}.DICT_INTERVIEW_TYPE.id"))
    chosen_date = Column(DateTime)
    interview_url = Column(Text)
    interview_code = Column(Text)
    feedback = Column(Text)
    is_confirmed = Column(Boolean, DefaultClause("1"), nullable=False)
    comment = Column(Text)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)

    user = relationship("User", foreign_keys=[user_id])
    administrator = relationship("Administrator", foreign_keys=[administrator_id])
    language = relationship("DictLanguage", foreign_keys=[language_id])
    interview_type = relationship("DictInterviewType", foreign_keys=[interview_type_id])