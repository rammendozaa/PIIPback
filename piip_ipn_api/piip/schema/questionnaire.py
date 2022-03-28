from piip.schema.base_schema import BaseSchema
from marshmallow import fields
from piip.models import Questionnaire


class QuestionnaireSchema(BaseSchema):
    __model__ = Questionnaire

    id = fields.Integer(dump_only=True)
    title = fields.String()
    questions = fields.String()
    questions_route = fields.String(data_key="questionsRoute")
    total_questions = fields.Integer(data_key="totalQuestions")
    answers = fields.String()
