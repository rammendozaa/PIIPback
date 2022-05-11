from piip.models import Problem
from piip.schema.base_schema import BaseSchema
from marshmallow import fields, post_dump
from marshmallow.utils import EXCLUDE

class ProblemSchema(BaseSchema):
    __model__ = Problem

    id = fields.Integer(data_key='id')
    title = fields.String()
    description = fields.String(data_key="description")
    time_limit = fields.String(data_key="time_limit")
    memory_limit = fields.String(data_key="memory_limit")
    source = fields.String(data_key="source")
    tags = fields.String(data_key="tags")
    url = fields.String(data_key="url")
    input = fields.String(data_key="input")
    output = fields.String(data_key="ouput")
    test_cases = fields.String(data_key="test_cases")
    finished_date = fields.String(data_key="finished_date")
    solution = fields.String(data_key= "solution")

    @post_dump
    def after_serialize(self, data, many, **kwargs):
        process_tags = data["tags"]
        tag_array = process_tags.split('_')
        data["tags"] = tag_array
        return data