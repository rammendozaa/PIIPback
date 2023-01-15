from flask import request
from flask_jwt_extended import jwt_required

from piip.command.constants import ACTIVITY_TYPES
from piip.command.ownership import mentor_only
from piip.command.questionnaire import (
    create_soft_skill_question, get_all_soft_skill_questions,
    get_all_unassigned_soft_skill_questions, get_soft_skill_question)
from piip.command.template import get_all_unassigned_activities_to_section
from piip.models.question import SoftSkillQuestion as Question
from piip.routes.resource import PIIPResource
from piip.schema.question import SoftSkillQuestionSchema


class SoftSkillQuestionRoute(PIIPResource):
    @jwt_required()
    def post(self):
        mentor_only(request)
        soft_skill_question_to_add = SoftSkillQuestionSchema().load(
            request.get_json(silent=True) or {}
        )
        return SoftSkillQuestionSchema().dump(
            create_soft_skill_question(soft_skill_question_to_add)
        )

    @jwt_required()
    def get(self):
        user_id = request.args.get("user_id", None)
        if user_id:
            return SoftSkillQuestionSchema(many=True).dump(
                get_all_unassigned_soft_skill_questions(user_id)
            )
        question_id = request.args.get("questionId", None)
        if question_id:
            return SoftSkillQuestionSchema().dump(get_soft_skill_question(question_id))
        section_id = request.args.get("sectionId", None)
        if section_id:
            return SoftSkillQuestionSchema(many=True).dump(
                get_all_unassigned_activities_to_section(
                    section_id, Question, ACTIVITY_TYPES["SOFT_SKILL_QUESTION"]
                )
            )
        return SoftSkillQuestionSchema(many=True).dump(get_all_soft_skill_questions())
