from flask import request
from flask_restful import Resource
from piip.schema.template import TemplateSchema
from piip.command.template import (
    add_template_section,
    add_template,
    add_section_activity,
    disable_template_by_id,
    disable_template_section_by_id,
    disable_template_activity_by_id,
)
from piip.schema.template import TemplateSectionSchema
from piip.query.template import (
    get_template_by_id,
    get_template_activity_by_id,
    get_template_section_by_id,
)
from piip.schema.template import TemplateActivitySchema


class Template(Resource):
    def get(self, template_id: int):
        return TemplateSchema().dump(get_template_by_id(template_id))
    
    def delete(self, template_id: int):
        return TemplateSchema().dump(disable_template_by_id(template_id))


class TemplateSection(Resource):
    def get(self, section_id: int):
        return TemplateSectionSchema().dump(get_template_section_by_id(section_id))
    
    def delete(self, section_id: int):
        return TemplateSectionSchema().dump(disable_template_section_by_id(section_id))


class SectionActivity(Resource):
    def get(self, activity_id: int):
        return TemplateActivitySchema().dump(get_template_activity_by_id(activity_id))
    
    def delete(self, activity_id: int):
        return TemplateActivitySchema().dump(disable_template_activity_by_id(activity_id))


class AddTemplate(Resource):
    def post(self):
        create_template = TemplateSchema().load(request.get_json(silent=True) or {})
        return TemplateSchema().dump(add_template(create_template))


class AddTemplateSection(Resource):
    def post(self, template_id: int):
        create_section = TemplateSectionSchema().load(
            request.get_json(silent=True) or {}
            )
        return TemplateSectionSchema().dump(
            add_template_section(template_id, create_section)
        )


class AddSectionActivity(Resource):
    def post(self, section_id: int):
        create_activity = TemplateActivitySchema().load(
            request.get_json(silent=True) or {}
        )
        return TemplateActivitySchema().dump(
            add_section_activity(section_id, create_activity)
        )