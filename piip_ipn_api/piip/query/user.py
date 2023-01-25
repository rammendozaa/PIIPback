from datetime import datetime

from piip.models.user import (UserTemplate, UserTemplateActivity,
                              UserTemplateSection)
from piip.services.database.setup import session


def get_user_template_by_id(user_template_id):
    return (
        session.query(UserTemplate)
        .filter(
            UserTemplate.is_active == True,
            UserTemplate.id == user_template_id,
        )
        .first()
    )


def get_user_template_section_by_id(user_template_section_id):
    return (
        session.query(UserTemplateSection)
        .filter(
            UserTemplateSection.is_active == True,
            UserTemplateSection.id == user_template_section_id,
        )
        .first()
    )


def get_user_template_activity_by_id(user_template_activity_id):
    return (
        session.query(UserTemplateActivity)
        .filter(
            UserTemplateActivity.is_active == True,
            UserTemplateActivity.id == user_template_activity_id,
        )
        .first()
    )


def get_active_templates_by_user_id(user_id):
    return (
        session.query(UserTemplate)
        .filter(
            UserTemplate.is_active == True,
            UserTemplate.user_id == user_id,
            UserTemplate.status_id != 4,
        )
        .order_by(
            UserTemplate.position.asc(),
        )
        .first()
    )


def verify_template_completion(user_template):
    if user_template:
        for section in user_template.user_sections:
            if section.status_id != 4:
                return
        user_template.status_id = 4
        session.add(user_template)
        session.commit()


def mark_user_template_section_in_progress(user_template_section):
    user_template_section.status_id = 2
    user_template_section.user_template.status_id = 2
    session.commit()


def verify_section_completion(user_template_section):
    if user_template_section:
        for activity in user_template_section.user_activities:
            if activity.status_id != 4:
                mark_user_template_section_in_progress(user_template_section)
                return
        user_template_section.status_id = 4
        session.add(user_template_section)
        session.commit()
        verify_template_completion(user_template_section.user_template)


def update_user_template_activity_by_id(user_template_activity_id, status_id):
    activity = session.query(UserTemplateActivity).get(user_template_activity_id)
    if not activity:
        return False
    if activity.status_id == status_id:
        return True
    if status_id == 4:
        activity.finished_date = datetime.now()
    if activity.status_id != 4:
        activity.status_id = status_id
    if status_id == 2 or status_id == 3:
        mark_user_template_section_in_progress(activity.user_template_section)
    if status_id == 4:
        verify_section_completion(activity.user_template_section)
    session.add(activity)
    session.commit()
    return True


def get_user(user_id):
    return session.query(User).get(user_id)
