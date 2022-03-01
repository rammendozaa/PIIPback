from piip.database_setup import PIIPModel

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey, 
    String,
    DateTime,
)
from sqlalchemy.orm import relationship


class CompanyTracking(PIIPModel):
    __tablename__ = "COMPANY_TRACKING"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("USER.id"), nullable=False)
    company_id = Column(Integer, ForeignKey("DICT_COMPANY.id"), nullable=False)
    status_id = Column(Integer,  ForeignKey("DICT_TRACKING_STATUS.id"), nullable=False)
    application_url = Column(String(255))
    interview_date = Column(DateTime)

    user = relationship("User", foreign_keys=[user_id])
    company = relationship("DictCompany", foreign_keys=[company_id])
    status = relationship("DictTrackingStatus", foreign_keys=[status_id])


class CompanyTrackingLinks(PIIPModel):
    __tablename__ = "COMPANY_TRACKING_LINKS"

    id = Column(Integer, primary_key=True)
    company_tracking_id = Column(Integer, ForeignKey("COMPANY_TRACKING.id"), nullable=False)
    description = Column(String(255), nullable=False)
    url = Column(String(1000), nullable=False)

    company_tracking = relationship("CompanyTracking", foreign_keys=[company_tracking_id])
