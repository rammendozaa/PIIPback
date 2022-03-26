from piip.models import Template
from piip.schema.base_schema import BaseSchema
from marshmallow import fields
from marshmallow.utils import EXCLUDE
from piip.models.template import TemplateSection
from piip.models.template import TemplateActivity


class TemplateActivitySchema(BaseSchema):
    __model__ = TemplateActivity

    id = fields.Integer(dump_only=True)
    name = fields.String()
    description = fields.String()
    position = fields.String()
    external_reference = fields.Integer()


class TemplateSectionSchema(BaseSchema):
    __model__ = TemplateSection

    class Meta:
        unknown = EXCLUDE

    id = fields.Integer(dump_only=True)
    name = fields.String()
    description = fields.String()
    position = fields.Integer()

    activities = fields.List(fields.Nested(TemplateActivitySchema))


class TemplateSchema(BaseSchema):
    __model__ = Template
    
    class Meta:
        unknown = EXCLUDE
    
    id = fields.Integer(dump_only=True)
    name = fields.String()
    description = fields.String()
    position = fields.Integer()

    sections = fields.List(fields.Nested(TemplateSectionSchema))