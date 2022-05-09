from piip.schema.base_schema import BaseSchema
from marshmallow import fields, post_dump
from piip.models import Interview


class InterviewSchema(BaseSchema):
    __model__ = Interview

    id = fields.Integer(dump_only=True)
    chosen_date = fields.DateTime(data_key="chosenDate")
    interview_url = fields.String(data_key="interviewUrl")
    interview_code = fields.String(data_key="interviewCode")
    feedback = fields.String()
    user_id = fields.Integer(data_key="userId")
    administrator_id = fields.Integer(data_key="administratorId")
    language_id = fields.Integer(data_key="languageId")
    is_confirmed = fields.Boolean(data_key="isConfirmed", missing=False)
    comment = fields.String()
    interview_type_id = fields.Integer()
    is_active = fields.Boolean(data_key="isActive")
