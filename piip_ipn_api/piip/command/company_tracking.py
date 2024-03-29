from piip.models.company_tracking import CompanyTracking, CompanyTrackingLinks
from piip.services.database.setup import session


def getInterviewData(_user_id):
    return session.query(CompanyTracking).filter_by(user_id=_user_id).all()


def get_company_tracking_for_user(user_id):
    return (
        session.query(CompanyTracking)
        .filter(
            CompanyTracking.user_id == user_id,
            CompanyTracking.is_active == True,
        )
        .all()
    )


def create_company_tracking_for_user(company_tracking):
    if company_tracking.status_id is None:
        company_tracking.status_id = 1
    session.add(company_tracking)
    session.commit()
    return company_tracking


def create_company_tracking_link(company_tracking_link):
    session.add(company_tracking_link)
    session.commit()
    return company_tracking_link


def delete_company_tracking_link(company_tracking_link_id):
    company_tracking_link = session.query(CompanyTrackingLinks).get(
        company_tracking_link_id
    )
    if not company_tracking_link:
        return False
    company_tracking_link.is_active = False
    session.add(company_tracking_link)
    session.commit()
    return True


def update_company_tracking_link(company_tracking_link_id, new_company_tracking_link):
    company_tracking_link = session.query(CompanyTrackingLinks).get(
        company_tracking_link_id
    )
    if not company_tracking_link:
        return False
    company_tracking_link.description = (
        new_company_tracking_link.description or company_tracking_link.description
    )
    company_tracking_link.url = (
        new_company_tracking_link.url or company_tracking_link.url
    )
    session.add(company_tracking_link)
    session.commit()
    return True


def delete_company_tracking(company_tracking_id):
    company_tracking = session.query(CompanyTracking).get(company_tracking_id)
    if not company_tracking:
        return False
    company_tracking.is_active = False
    session.add(company_tracking)
    session.commit()
    return True


def update_company_tracking(company_tracking_id, new_company_tracking):
    company_tracking = session.query(CompanyTracking).get(company_tracking_id)
    if not company_tracking:
        return False
    company_tracking.status_id = (
        new_company_tracking.status_id or company_tracking.status_id
    )
    company_tracking.interview_date = (
        new_company_tracking.interview_date or company_tracking.interview_date
    )
    session.add(company_tracking)
    session.commit()
    return True
