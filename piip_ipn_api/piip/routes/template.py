from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from piip.command.template import (add_section_activity, add_template,
                                   add_template_section,
                                   disable_template_activity_by_id,
                                   disable_template_by_id,
                                   disable_template_section_by_id)
from piip.query.template import (get_active_templates,
                                 get_template_activity_by_id,
                                 get_template_by_id,
                                 get_template_section_by_id)
from piip.schema.template import (TemplateActivitySchema, TemplateSchema,
                                  TemplateSectionSchema)


class Template(Resource):
    @jwt_required()
    def get(self):
        template_id = request.args.get("template_id", None)
        if template_id:
            return TemplateSchema().dump(get_template_by_id(template_id))
        return TemplateSchema(many=True).dump(get_active_templates())

    @jwt_required()
    def delete(self):
        template_id = request.args.get("template_id", None)
        return TemplateSchema().dump(disable_template_by_id(template_id))


class TemplateSection(Resource):
    @jwt_required()
    def get(self, section_id: int):
        return TemplateSectionSchema().dump(get_template_section_by_id(section_id))

    @jwt_required()
    def delete(self, section_id: int):
        return TemplateSectionSchema().dump(disable_template_section_by_id(section_id))


class SectionActivity(Resource):
    @jwt_required()
    def get(self, activity_id: int):
        return TemplateActivitySchema().dump(get_template_activity_by_id(activity_id))

    @jwt_required()
    def delete(self, activity_id: int):
        return TemplateActivitySchema().dump(
            disable_template_activity_by_id(activity_id)
        )


class AddTemplate(Resource):
    @jwt_required()
    def post(self):
        create_template = TemplateSchema().load(request.get_json(silent=True) or {})
        return TemplateSchema().dump(add_template(create_template))


class AddTemplateSection(Resource):
    @jwt_required()
    def post(self, template_id: int):
        create_section = TemplateSectionSchema().load(
            request.get_json(silent=True) or {}
        )
        return TemplateSectionSchema().dump(
            add_template_section(template_id, create_section)
        )


class AddSectionActivity(Resource):
    @jwt_required()
    def post(self, section_id: int):
        create_activity = TemplateActivitySchema().load(
            request.get_json(silent=True) or {}
        )
        return TemplateActivitySchema().dump(
            add_section_activity(section_id, create_activity)
        )
