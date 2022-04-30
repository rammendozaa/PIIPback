from piip.services.database.setup import session
from piip.models.user import (
    UserTemplate,
    UserTemplateSection,
    UserTemplateActivity,
)

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
    return (session.query(UserTemplate)
        .filter(
            UserTemplate.is_active == True,
            UserTemplate.user_id == user_id,
            UserTemplate.status_id == 1,
        )
        .order_by(
            UserTemplate.position.asc(),
        )
        .first()
    )


def update_user_template_activity_by_id(user_template_activity_id, status_id):
        activity = session.query(UserTemplateActivity).get(user_template_activity_id)
        if not activity:
            return False
        activity.status_id = status_id
        session.add(activity)
        session.commit()
        return True
