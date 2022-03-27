from piip.models import Template, TemplateActivity, TemplateSection
from piip.services.database.setup import session


def get_template_by_id(template_id):
    return (
        session.query(Template)
        .join(TemplateSection, TemplateSection.template_id == Template.id)
        .join(TemplateActivity, TemplateActivity.template_section_id == TemplateSection.id)
        .filter(
            Template.id == template_id,
            Template.is_active == 1,
            TemplateSection.is_active == 1,
            TemplateActivity.is_active == 1
        )
        .first()
    )
