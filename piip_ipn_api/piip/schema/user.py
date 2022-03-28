from piip.models import User
from piip.schema.base_schema import BaseSchema
from marshmallow import fields
from marshmallow.utils import EXCLUDE

class UserSchema(BaseSchema):
    __model__ = User

    class Meta:
        unknown = EXCLUDE

    id = fields.String(data_key="id") 
    email = fields.String(data_key="email")
    first_name = fields.String(data_key="first_name")
    last_name = fields.String(data_key="last_name")
    school_id = fields.String(data_key="school_id")
