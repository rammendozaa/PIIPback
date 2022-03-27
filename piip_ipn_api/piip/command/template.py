from piip.query.template import get_template_by_id
from piip.models import TemplateActivity, TemplateSection, Template
from piip.services.database.setup import session


def update_template_by_id(template_id, updates):
    return get_template_by_id(template_id)


def add_template(template_to_add):
    template = Template(
        name=template_to_add.name,
        description=template_to_add.description
    )
    session.add(template)
    session.commit()
    for section in template_to_add.sections:
        new_section = TemplateSection(
            name=section.name,
            description=section.description,
            position=section.position,
            template=template,
        )
        session.add(new_section)
        session.commit()
        for activity in section.activities:
            new_activity = TemplateActivity(
                name=activity.name,
                description=activity.description,
                template_section=new_section,
                position=activity.position,
                activity_type_id=activity.activity_type_id,
                external_reference=activity.external_reference,
            )
            session.add(new_activity)
            session.commit()
    return template
