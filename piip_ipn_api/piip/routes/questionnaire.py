from flask import request
from flask_jwt_extended import jwt_required

from piip.command.constants import ACTIVITY_TYPES
from piip.command.questionnaire import insert_questionnaire
from piip.command.template import get_all_unassigned_activities_to_section
from piip.models.questionnaire import Questionnaire
from piip.query.questionnaire import (get_questionnaire_by_id,
                                      get_questionnaires,
                                      get_unassigned_questionnaires)
from piip.routes.resource import PIIPResource
from piip.schema.questionnaire import (CreateQuestionnaireSchema,
                                       QuestionnaireSchema)


class QuestionnaireRoute(PIIPResource):
    @jwt_required()
    def get(self):
        user_id = request.args.get("user_id", None)
        if user_id:
            return QuestionnaireSchema(many=True).dump(
                get_unassigned_questionnaires(user_id)
            )
        questionnaire_id = request.args.get("questionnaireId", None)
        if questionnaire_id:
            return QuestionnaireSchema().dump(get_questionnaire_by_id(questionnaire_id))
        section_id = request.args.get("sectionId", None)
        if section_id:
            return QuestionnaireSchema(many=True).dump(
                get_all_unassigned_activities_to_section(
                    section_id, Questionnaire, ACTIVITY_TYPES["QUESTIONNAIRE"]
                )
            )
        return QuestionnaireSchema(many=True).dump(get_questionnaires())

    @jwt_required()
    def post(self):
        create_questionnaire = CreateQuestionnaireSchema().load(
            request.get_json(silent=True) or {}
        )
        return QuestionnaireSchema().dump(insert_questionnaire(create_questionnaire))
