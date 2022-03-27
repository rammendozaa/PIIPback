from piip.models.database_setup import PIIPModel

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey, 
    String,
    DateTime,
    DefaultClause,
    Boolean,
)
from sqlalchemy.orm import relationship
from piip.models.constants import DATABASE


class CompanyTracking(PIIPModel):
    __tablename__ = "COMPANY_TRACKING"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(f"{DATABASE}.USER.id"), nullable=False)
    company_id = Column(Integer, ForeignKey(f"{DATABASE}.DICT_COMPANY.id"), nullable=False)
    status_id = Column(Integer,  ForeignKey(f"{DATABASE}.DICT_TRACKING_STATUS.id"), nullable=False)
    application_url = Column(String(255))
    interview_date = Column(DateTime)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)

    user = relationship("User", foreign_keys=[user_id])
    company = relationship("DictCompany", foreign_keys=[company_id])
    status = relationship("DictTrackingStatus", foreign_keys=[status_id])


class CompanyTrackingLinks(PIIPModel):
    __tablename__ = "COMPANY_TRACKING_LINKS"

    id = Column(Integer, primary_key=True)
    company_tracking_id = Column(Integer, ForeignKey(f"{DATABASE}.COMPANY_TRACKING.id"), nullable=False)
    description = Column(String(255), nullable=False)
    url = Column(String(1000), nullable=False)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)

    company_tracking = relationship("CompanyTracking", foreign_keys=[company_tracking_id])
