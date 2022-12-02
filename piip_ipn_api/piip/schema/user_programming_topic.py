from marshmallow import fields

from piip.models.user import UserProgrammingTopic
from piip.schema.base_schema import BaseSchema


class UserProgrammingTopicSchema(BaseSchema):
    __model__ = UserProgrammingTopic

    id = fields.Integer(data_key="id")
    user_id = fields.String(data_key="user_id")
    programming_topic_id = fields.String(data_key="programming_topic_id")
    status_id = fields.Integer(data_key="status_id")
