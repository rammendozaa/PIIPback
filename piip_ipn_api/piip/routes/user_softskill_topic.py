from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
from piip.command.user_programming_topic import getNumberOfProgrammingTopicsSolved


class GetNumberOfSoftSkillTopicsSolvedByUser(Resource):
    @jwt_required()
    def post(self):
        numberOfProblems = getNumberOfProgrammingTopicsSolved(request.form.get("user_id", default='',type=str))
        return {"numberOfProgrammingTopics": numberOfProblems}

