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

    class Meta:
        unknown = EXCLUDE

    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    position = fields.Integer()

    activities = fields.List(fields.Nested(TemplateActivitySchema))


class TemplateSchema(BaseSchema):
    __model__ = Template
    
    class Meta:
        unknown = EXCLUDE
    
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    position = fields.Integer()

    sections = fields.List(fields.Nested(TemplateSectionSchema))
