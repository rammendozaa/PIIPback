from flask import request
from piip.query.questionnaire import get_questionnaires
from flask_restful import Resource
from piip.schema.questionnaire import QuestionnaireSchema
from piip.schema.questionnaire import CreateQuestionnaireSchema
from piip.command.questionnaire import insert_questionnaire

class Questionnaire(Resource):
    def get(self):
        return QuestionnaireSchema(many=True).dump(get_questionnaires())

    def post(self):
        create_questionnaire = CreateQuestionnaireSchema().load(request.get_json(silent=True) or {})
        return QuestionnaireSchema().dump(insert_questionnaire(create_questionnaire))