import time
from datetime import datetime
from dateutil import tz
from piip.services.database.setup import session
from piip.models.company_tracking import (
    CompanyTrackingLinks,
    CompanyTracking,
)
def get_company_tracking_for_user(user_id):
    return (
        session.query(CompanyTracking)
        .join(CompanyTrackingLinks, CompanyTrackingLinks.company_tracking_id == CompanyTracking.id)
        .filter(
            CompanyTrackingLinks.is_active == 1,
            CompanyTracking.user_id == user_id,
        )
        .all()
    )


def create_company_tracking_for_user(company_tracking):
    if company_tracking.interview_date:
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()
        d = time.strptime(company_tracking.interview_date[:-1], "%Y-%m-%dT%H:%M:%S.%f")
        utc_str = time.strftime("%Y-%m-%d %H:%M:%S", d)
        utc = datetime.strptime(utc_str, '%Y-%m-%d %H:%M:%S')
        utc = utc.replace(tzinfo=from_zone)
        central = utc.astimezone(to_zone)
        company_tracking.interview_date = central.strftime("%Y-%m-%d %H:%M:%S")
    session.add(company_tracking)
    session.commit()


def create_company_tracking_link(company_tracking_link):
    session.add(company_tracking_link)
    session.commit()
    return company_tracking_link

def delete_company_tracking_link(company_tracking_link_id):
    company_tracking_link = (
        session.query(CompanyTrackingLinks).get(company_tracking_link_id)
    )
    if not company_tracking_link:
        return False
    company_tracking_link.is_active = False
    session.add(company_tracking_link)
    session.commit()
    return True


def update_company_tracking_link(company_tracking_link_id, description, url):
    company_tracking_link = (
        session.query(CompanyTrackingLinks).get(company_tracking_link_id)
    )
    if not company_tracking_link:
        return False
    company_tracking_link.description = description
    company_tracking_link.url = url
    session.add(company_tracking_link)
    session.commit()
