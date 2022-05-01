from flask_restful import Resource
from flask import request
from piip.command.questionnaire import create_soft_skill_question
from piip.schema.question import SoftSkillQuestionSchema


class SoftSkillQuestion(Resource):
    def post(self):
        soft_skill_question_to_add = SoftSkillQuestionSchema().load(request.get_json(silent=True) or {})
        return SoftSkillQuestionSchema().dump(create_soft_skill_question(soft_skill_question_to_add))
