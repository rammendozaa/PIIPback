from piip.models import Problem
from piip.schema.base_schema import BaseSchema
from marshmallow import fields
from marshmallow.utils import EXCLUDE

class UserProblemSchema(BaseSchema):
    __model__ = Problem

    id = fields.Integer(data_key='id')
    user_id = fields.String(data_key='user_id')
    problem_id = fields.String(data_key="problem_id")
    status_id = fields.String(data_key="status_id")
    status_id = fields.String(data_key="finished_id")