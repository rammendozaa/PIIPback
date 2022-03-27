from flask import request
from flask_restful import Resource
from piip.schema.template import TemplateSchema
from piip.query.template import get_template_by_id
from piip.command.template import update_template_by_id, add_template


class Template(Resource):
    def get(self, template_id: int):
        return TemplateSchema().dump(get_template_by_id(template_id))
    
    def put(self, template_id: int):
        updates = request.get_json(silent=True) or {}
        return TemplateSchema().dump(update_template_by_id(template_id, updates))


class AddTemplate(Resource):
    def post(self):
        print(request.get_json(silent=True))
        create_template = TemplateSchema().load(request.get_json(silent=True) or {})
        return TemplateSchema().dump(add_template(create_template))
