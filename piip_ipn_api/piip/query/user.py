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
    return (
        session.query(UserTemplate)
        .join(
            UserTemplateSection, UserTemplateSection.user_template_id == UserTemplate.id
        )
        .join(
            UserTemplateActivity, UserTemplateActivity.user_template_section_id == UserTemplateSection.id
        )
        .filter(
            UserTemplate.is_active == True,
            UserTemplateSection.is_active == True,
            UserTemplateActivity.is_active == True,
            UserTemplate.user_id == user_id,
            UserTemplateSection.user_id == user_id,
            UserTemplateActivity.user_id == user_id,
        )
        .order_by(
            UserTemplate.position.desc(),
            UserTemplateSection.position.desc(),
            UserTemplateActivity.position.desc(),
        )
        .all()
    )
