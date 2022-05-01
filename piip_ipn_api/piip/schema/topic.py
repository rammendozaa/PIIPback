from piip.schema.base_schema import BaseSchema
from marshmallow import fields
from piip.models import (
    ProgrammingTopic,
    SoftSkillTopic,
)


class ProgrammingTopicSchema(BaseSchema):
    __model__ = ProgrammingTopic

    id = fields.Integer(dump_only=True)
    title = fields.String()
    description = fields.String()
    topic_information = fields.String()


class SoftSkillTopicSchema(BaseSchema):
    __model__ = SoftSkillTopic

    id = fields.Integer(dump_only=True)
    title = fields.String()
    description = fields.String()
    topic_information = fields.String()
