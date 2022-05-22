from flask import request
from piip.query.questionnaire import (
    get_questionnaires,
    get_questionnaire_by_id,
    get_unassigned_questionnaires,
)
from flask_restful import Resource
from piip.schema.questionnaire import QuestionnaireSchema
from piip.schema.questionnaire import CreateQuestionnaireSchema
from piip.command.questionnaire import insert_questionnaire

class Questionnaire(Resource):
    def get(self):
        user_id = request.args.get("user_id", None)
        if user_id:
            return QuestionnaireSchema(many=True).dump(get_unassigned_questionnaires(user_id))
        questionnaire_id = request.args.get("questionnaireId", None)
        if questionnaire_id:
            return QuestionnaireSchema().dump(get_questionnaire_by_id(questionnaire_id))
        return QuestionnaireSchema(many=True).dump(get_questionnaires())

    def post(self):
        create_questionnaire = CreateQuestionnaireSchema().load(request.get_json(silent=True) or {})
        return QuestionnaireSchema().dump(insert_questionnaire(create_questionnaire))