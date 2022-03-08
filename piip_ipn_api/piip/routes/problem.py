from piip.services.providers.codeforces.codeforces import Codeforces
from flask_restful import Resource
from flask import request, jsonify
import random
from flask_jwt_extended import jwt_required
from piip.command.problem import get_all_problems
from piip.schema.problem import ProblemSchema


CF_USERNAME = ""
CF_PASSWORD = ""

class Problems(Resource):
    # @jwt_required()
    def get(self):
        return jsonify(ProblemSchema(many=True).dump(get_all_problems()))
        """
            [
            {"title" : "p1", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
            {"title" : "p3", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
            {"title" : "p2", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
        ])
        """

class SubmitProblem(Resource):
    def post(self, problem_id: int):
        codeforces = Codeforces()
        codeforces.login(CF_USERNAME, CF_PASSWORD)
        if codeforces.check_login():
            submissionUrl = codeforces.submit('1254A', 'qwer' + str(random.random()) )
            return {"submissionUrl": submissionUrl}
        else:
            return {"submissionUrl": "failed"}


class Submission(Resource):
    def post(self):
        submissionUrl = request.args.get('submissionUrl',default='',type=str)
        codeforces = Codeforces()
        codeforces.login(CF_USERNAME, CF_PASSWORD)
        if codeforces.check_login():
            status = codeforces.getSubmissionStatus(submissionUrl)
            return {"status": status}
        else:
            return {"status": "failed to login"}

