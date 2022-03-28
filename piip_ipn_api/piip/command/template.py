from piip.models import TemplateActivity, TemplateSection, Template
from piip.services.database.setup import session
from piip.query.template import (
    get_template_activity_by_id,
    get_template_section_by_id,
    get_template_by_id,
)


def disable_template_by_id(template_id):
    template = get_template_by_id(template_id)
    if not template:
        raise "Template not found"
    template.is_active = False
    session.add(template)
    session.commit()
    return template


def disable_template_section_by_id(section_id):
    section = get_template_section_by_id(section_id)
    if not section:
        raise "Template section not found"
    section.is_active = False
    session.add(section)
    session.commit()
    return section


def disable_template_activity_by_id(activity_id):
    activity = get_template_activity_by_id(activity_id)
    if not activity:
        raise "Template activity not found"
    activity.is_active = False
    session.add(activity)
    session.commit()
    return activity


def add_section_activity(section_id, activity_to_add):
    new_activity = TemplateActivity(
        name=activity_to_add.name,
        description=activity_to_add.description,
        template_section_id=section_id,
        position=activity_to_add.position,
        activity_type_id=activity_to_add.activity_type_id,
        external_reference=activity_to_add.external_reference,
    )
    session.add(new_activity)
    session.commit()
    return new_activity


def add_template_section(template_id, section_to_add):
    new_section = TemplateSection(
        name=section_to_add.name,
        description=section_to_add.description,
        position=section_to_add.position,
        template_id=template_id,
    )
    session.add(new_section)
    session.commit()
    for activity in section_to_add.activities:
        add_section_activity(new_section.id, activity)
    return new_section


def add_template(template_to_add):
    template = Template(
        name=template_to_add.name,
        description=template_to_add.description
    )
    session.add(template)
    session.commit()
    for section in template_to_add.sections:
        add_template_section(template.id, section)
    return template
