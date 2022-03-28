from marshmallow import fields
from piip.models import SoftSkillQuestion
from piip.schema.base_schema import BaseSchema

class SoftSkillQuestionSchema(BaseSchema):
    __model__ = SoftSkillQuestion

    id = fields.Integer(dump_only=True)
    title = fields.String()
    question = fields.String()
    file_route = fields.String(data_key="fileRoute")
    information = fields.String()
