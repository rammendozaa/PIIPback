from flask_restful import Resource
from piip.schema.template import TemplateSchema
from piip.query.template import get_template_by_id


class Template(Resource):
    def get(self, template_id: int):
        return TemplateSchema().dump(get_template_by_id(template_id))
    