from flask import request
from flask_restful import Resource
from piip.schema.template import TemplateSchema
from piip.query.template import get_template_by_id
from piip.command.template import add_template_section, disable_template_by_id, add_template
from piip.schema.template import TemplateSectionSchema


class Template(Resource):
    def get(self, template_id: int):
        return TemplateSchema().dump(get_template_by_id(template_id))
    
    def delete(self, template_id: int):
        return TemplateSchema().dump(disable_template_by_id(template_id))


class AddTemplate(Resource):
    def post(self):
        create_template = TemplateSchema().load(request.get_json(silent=True) or {})
        return TemplateSchema().dump(add_template(create_template))


class TemplateSection(Resource):
    def post(self, template_id: int):
        create_section = TemplateSectionSchema().load(request.get_json(silent=True) or {})
        return TemplateSectionSchema().dump(add_template_section(template_id, create_section))
