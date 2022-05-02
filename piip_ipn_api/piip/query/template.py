from piip.models import (
    Template,
    TemplateActivity,
    TemplateSection,
)
from piip.services.database.setup import session


def get_template_by_id(template_id):
    return session.query(Template).filter(Template.id == template_id, Template.is_active == True).first()

    """
    return (
        session.query(Template)
        .join(TemplateSection, TemplateSection.template_id == Template.id)
        .join(TemplateActivity, TemplateActivity.template_section_id == TemplateSection.id)
        .filter(
            Template.id == template_id,
            Template.is_active == True,
            TemplateSection.is_active == True,
            TemplateActivity.is_active == True
        )
        .first()
    )
    """


def get_template_section_by_id(section_id):
    return (
        session.query(TemplateSection)
        .join(TemplateActivity, TemplateActivity.template_section_id == TemplateSection.id)
        .filter(
            TemplateSection.id == section_id,
            TemplateSection.is_active == True,
            TemplateActivity.is_active == True
        )
        .first() 
    )


def get_template_activity_by_id(activity_id):
    return (
        session.query(TemplateActivity)
        .filter(
            TemplateActivity.is_active == True,
            TemplateActivity.id == activity_id
        )
        .first()
    )