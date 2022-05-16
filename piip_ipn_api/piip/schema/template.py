from piip.models import (
    Template,
    TemplateSection,
    TemplateActivity
)
from piip.schema.base_schema import BaseSchema
from marshmallow import fields, post_dump
from marshmallow.utils import EXCLUDE
from piip.services.database.setup import session
from piip.schema.constants import ACTIVITY_TYPE_TO_MODEL, ACTIVITY_TYPE_TO_SCHEMA

class TemplateActivitySchema(BaseSchema):
    __model__ = TemplateActivity

    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    position = fields.Integer()
    activity_type_id = fields.Integer(data_key="activityType")
    external_reference = fields.Integer(data_key="externalReference")
    is_active = fields.Boolean()

    @post_dump
    def after_serialize(self, data, many, **kwargs):
        activity_type = data.get("activityType", None)
        external_reference = data.get("externalReference", None)
        if (activity_type and external_reference):
            activity_schema = ACTIVITY_TYPE_TO_SCHEMA.get(activity_type)
            activity_class = ACTIVITY_TYPE_TO_MODEL.get(activity_type)
            activity = session.query(activity_class).get(external_reference)
            data["activity"] = activity_schema().dump(activity)
        return data


class TemplateSectionSchema(BaseSchema):
    __model__ = TemplateSection

    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    position = fields.Integer()
    is_active = fields.Boolean()

    activities = fields.List(fields.Nested(TemplateActivitySchema))

    @post_dump
    def after_serialize(self, data, many, **kwargs):
        activities = data["activities"]
        if activities:
            data["activities"] = list(filter(lambda x: x["is_active"] == True, activities))
        return data


class TemplateSchema(BaseSchema):
    __model__ = Template
        
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    position = fields.Integer()
    is_active = fields.Boolean()

    sections = fields.List(fields.Nested(TemplateSectionSchema))

    @post_dump
    def after_serialize(self, data, many, **kwargs):
        sections = data["sections"]
        if sections:
            data["sections"] = list(filter(lambda x: x["is_active"] == True, sections))
        return data