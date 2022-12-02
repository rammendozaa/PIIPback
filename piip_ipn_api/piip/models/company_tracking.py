from typing import List

from sqlalchemy import (Boolean, Column, DateTime, DefaultClause, ForeignKey,
                        Integer, String)
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import RelationshipProperty
from sqlalchemy.sql import func

from piip.models.constants import DATABASE
from piip.models.database_setup import PIIPModel


class CompanyTrackingLinks(PIIPModel):
    __tablename__ = "COMPANY_TRACKING_LINKS"

    id = Column(Integer, primary_key=True)
    company_tracking_id = Column(
        Integer, ForeignKey(f"{DATABASE}.COMPANY_TRACKING.id"), nullable=False
    )
    description = Column(String(255), nullable=False)
    url = Column(String(1000), nullable=False)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)

    company_tracking = relationship(
        "CompanyTracking",
        foreign_keys=[company_tracking_id],
        back_populates="tracking_links",
    )


class CompanyTracking(PIIPModel):
    __tablename__ = "COMPANY_TRACKING"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(f"{DATABASE}.USER.id"), nullable=False)
    company_id = Column(
        Integer, ForeignKey(f"{DATABASE}.DICT_COMPANY.id"), nullable=False
    )
    status_id = Column(
        Integer, ForeignKey(f"{DATABASE}.DICT_TRACKING_STATUS.id"), nullable=False
    )
    application_url = Column(String(255))
    interview_date = Column(DateTime)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_date = Column(DateTime, DefaultClause(func.now()))

    user = relationship("User", foreign_keys=[user_id])
    company = relationship("DictCompany", foreign_keys=[company_id])
    status = relationship("DictTrackingStatus", foreign_keys=[status_id])

    tracking_links: "RelationshipProperty[List[CompanyTrackingLinks]]" = relationship(
        "CompanyTrackingLinks", back_populates="company_tracking", lazy="dynamic"
    )
