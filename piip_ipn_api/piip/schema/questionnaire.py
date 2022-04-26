from piip.schema.base_schema import BaseSchema, DataclassSchema
from marshmallow import fields, post_dump
from piip.models.questionnaire import (
    Questionnaire,
    QuestionnaireQuestion,
    CreateQuestionnaire,
)


class QuestionnaireQuestionSchema(BaseSchema):
    __model__ = QuestionnaireQuestion

    question = fields.String(data_key="questionText")
    answer = fields.String()
    option_1 = fields.String()
    option_2 = fields.String()
    option_3 = fields.String()

    @post_dump
    def after_serialize(self, data, many, **kwargs):
        answer_options = []
        answer = {
            "answerText": data["answer"],
            "isCorrect": True,
        }
        answer_options.append(answer)
        answer = {
            "answerText": data["option_1"],
            "isCorrect": True,
        }
        answer_options.append(answer)
        answer = {
            "answerText": data["option_2"],
            "isCorrect": True,
        }
        answer_options.append(answer)
        answer = {
            "answerText": data["option_3"],
            "isCorrect": True,
        }
        answer_options.append(answer)
        data["answerOptions"] = answer_options
        del data["answer"]
        del data["option_1"]
        del data["option_2"]
        del data["option_3"]
        return data


class QuestionnaireSchema(BaseSchema):
    __model__ = Questionnaire

    id = fields.Integer(dump_only=True)
    title = fields.String()
    description = fields.String()
    total_questions = fields.Integer(data_key="totalQuestions")
    
    questions = fields.List(fields.Nested(QuestionnaireQuestionSchema))


class CreateQuestionnaireSchema(DataclassSchema):
    __model__ = CreateQuestionnaire

    title = fields.String()
    description = fields.String()
    questions = fields.List(fields.Dict, data_key="questions")
