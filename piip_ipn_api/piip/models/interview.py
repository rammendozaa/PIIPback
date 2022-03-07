from piip.database_setup import PIIPModel
from sqlalchemy import (
    Column, 
    DateTime, 
    ForeignKey, 
    Integer, 
    Text,
)
from piip.models import User, Administrator, DictLanguage
from sqlalchemy.orm import relationship


class Interview(PIIPModel):
    __tablename__ = "INTERVIEW"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    administrator_id = Column(Integer, ForeignKey(Administrator.id))
    language_id = Column(Integer, ForeignKey(DictLanguage.id))
    chosen_date = Column(DateTime)
    interview_url = Column(Text)
    interview_code = Column(Text)
    feedback = Column(Text)

    user = relationship("User", foreign_key=[user_id])
    administrator = relationship("Administrator", foreign_key=[administrator_id])
    language = relationship("DictLanguage", foreign_key=[language_id])
