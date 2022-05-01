from piip.models.user import UserProblem
from piip.schema.base_schema import BaseSchema
from marshmallow import fields
from marshmallow.utils import EXCLUDE

class UserProblemSchema(BaseSchema):
    __model__ = UserProblem

    id = fields.Integer(data_key='id')
    user_id = fields.String(data_key='user_id')
    problem_id = fields.String(data_key="problem_id")
    status_id = fields.String(data_key="status_id")
    finished_date = fields.String(data_key="finished_date")