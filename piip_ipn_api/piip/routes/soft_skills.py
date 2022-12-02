from flask import request
from flask_restful import Resource

from piip.command.questionnaire import (
    create_soft_skill_question, get_all_soft_skill_questions,
    get_all_unassigned_soft_skill_questions, get_soft_skill_question)
from piip.schema.question import SoftSkillQuestionSchema


class SoftSkillQuestion(Resource):
    def post(self):
        soft_skill_question_to_add = SoftSkillQuestionSchema().load(
            request.get_json(silent=True) or {}
        )
        return SoftSkillQuestionSchema().dump(
            create_soft_skill_question(soft_skill_question_to_add)
        )

    def get(self):
        user_id = request.args.get("user_id", None)
        if user_id:
            return SoftSkillQuestionSchema(many=True).dump(
                get_all_unassigned_soft_skill_questions(user_id)
            )
        question_id = request.args.get("questionId", None)
        if question_id:
            return SoftSkillQuestionSchema().dump(get_soft_skill_question(question_id))
        return SoftSkillQuestionSchema(many=True).dump(get_all_soft_skill_questions())
