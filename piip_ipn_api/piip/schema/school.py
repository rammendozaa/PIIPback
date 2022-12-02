from marshmallow import fields

from piip.models import DictSchool
from piip.schema.base_schema import BaseSchema


class SchoolSchema(BaseSchema):
    __model__ = DictSchool

    id = fields.String(data_key="id")
    name = fields.String(data_key="name")
