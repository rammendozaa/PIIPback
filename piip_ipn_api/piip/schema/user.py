from piip.models.user import (
    User,
    UserTemplate,
    UserTemplateSection,
    UserTemplateActivity,
)
from piip.schema.base_schema import BaseSchema
from marshmallow import fields, post_dump
from marshmallow.utils import EXCLUDE
from piip.schema.template import (
    TemplateSchema,
    TemplateActivitySchema,
    TemplateSectionSchema,
)

class UserSchema(BaseSchema):
    __model__ = User

    class Meta:
        unknown = EXCLUDE

    id = fields.String(data_key="id") 
    email = fields.String(data_key="email")
    first_name = fields.String(data_key="first_name")
    last_name = fields.String(data_key="last_name")
    school_id = fields.String(data_key="school_id")


class UserTemplateActivitySchema(BaseSchema):
    __model__ = UserTemplateActivity

    id = fields.Integer()
    template_activity = fields.Nested(TemplateActivitySchema)
    status_id = fields.Integer()
    position = fields.Integer()


class UserTemplateSectionSchema(BaseSchema):
    __model__ = UserTemplateSection

    id = fields.Integer()
    template_section = fields.Nested(TemplateSectionSchema)
    status_id = fields.Integer()
    position = fields.Integer()

    user_activities = fields.List(fields.Nested(
        UserTemplateActivitySchema
    ))

    @post_dump
    def after_serialize(self, data, many, **kwargs):
        del data["template_section"]["activities"]
        return data


class UserTemplateSchema(BaseSchema):
    __model__ = UserTemplate

    id = fields.Integer()
    template = fields.Nested(TemplateSchema)
    status_id = fields.Integer()
    position = fields.Integer()

    user_sections = fields.List(fields.Nested(
        UserTemplateSectionSchema
    ))

    @post_dump
    def after_serialize(self, data, many, **kwargs):
        del data["template"]["sections"]
        return data