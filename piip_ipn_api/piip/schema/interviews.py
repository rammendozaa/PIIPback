from piip.schema.base_schema import BaseSchema
from marshmallow import fields, post_dump
from piip.models import Interview
from piip.models.user import User
from piip.services.database.setup import session


class InterviewSchema(BaseSchema):
    __model__ = Interview

    id = fields.Integer(dump_only=True)
    chosen_date = fields.DateTime(data_key="chosenDate", required=False,allow_none=True)
    interview_url = fields.String(data_key="interviewUrl", required=False,allow_none=True)
    interview_code = fields.String(data_key="interviewCode", required=False,allow_none=True)
    feedback = fields.String(required=False,allow_none=True)
    user_id = fields.Integer(data_key="userId", required=False,allow_none=True)
    administrator_id = fields.Integer(data_key="administratorId", required=False,allow_none=True)
    language_id = fields.Integer(data_key="languageId", required=False,allow_none=True)
    is_confirmed = fields.Boolean(data_key="isConfirmed", missing=False, required=False,allow_none=True)
    comment = fields.String(required=False,allow_none=True)
    interview_type_id = fields.Integer(required=False,allow_none=True)
    is_active = fields.Boolean(dump_only=True, data_key="isActive")

    @post_dump
    def after_serialize(self, data, many, **kwargs):
        from piip.schema.user import UserSchema

        user_id = data["userId"]
        user = session.query(User).get(user_id)
        user_schema = UserSchema().dump(user)
        data["user"] = user_schema
        return data
