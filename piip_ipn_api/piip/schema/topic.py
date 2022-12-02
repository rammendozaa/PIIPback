from marshmallow import fields

from piip.models import ProgrammingTopic, SoftSkillTopic
from piip.schema.base_schema import BaseSchema


class ProgrammingTopicSchema(BaseSchema):
    __model__ = ProgrammingTopic

    id = fields.Integer(dump_only=True)
    title = fields.String()
    description = fields.String()
    topic_information = fields.String(data_key="topicInformation")
    created_by = fields.Integer(data_key="createdBy")


class SoftSkillTopicSchema(BaseSchema):
    __model__ = SoftSkillTopic

    id = fields.Integer(dump_only=True)
    title = fields.String()
    description = fields.String()
    topic_information = fields.String(data_key="topicInformation")
    created_by = fields.Integer(data_key="createdBy")
