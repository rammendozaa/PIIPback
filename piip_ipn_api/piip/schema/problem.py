from attr import fields
from piip.models import Problem
from piip.schema.base_schema import BaseSchema
from marshmallow import fields
from marshmallow.utils import EXCLUDE

class ProblemSchema(BaseSchema):
    __model__ = Problem

    class Meta:
        unknown = EXCLUDE

    id = fields.String(data_key='id')
    title = fields.String()
    description = fields.String(data_key="description")
    time_limit = fields.String(data_key="related_topics")
    memory_limit = fields.String(data_key="difficulty")
    category_id = fields.String(data_key="status")
    url = fields.String(data_key="url")
