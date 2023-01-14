from flask import jsonify, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from piip.command.problem import (get_all_problems,
                                  get_all_unassigned_problems, getProblem,
                                  getProblemCode, getRecommendations)
from piip.schema.problem import ProblemSchema
from piip.services.providers.codeforces.codeforces import Codeforces
from piip.services.providers.codeforces.codeforcesCrawler import \
    CodeforcesSpider

CF_USERNAME = "piip_ipn"
CF_PASSWORD = "*&WcgpYU4-.{mt.-"


class GetRecommendations(Resource):
    @jwt_required()
    def post(self):
        return jsonify(ProblemSchema(many=True).dump(getRecommendations()))


class Problems(Resource):
    @jwt_required()
    def get(self):
        user_id = request.args.get("user_id", None)
        if user_id:
            return jsonify(
                ProblemSchema(many=True).dump(get_all_unassigned_problems(user_id))
            )
        return jsonify(ProblemSchema(many=True).dump(get_all_problems()))
        """
            [
            {"title" : "p1", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
            {"title" : "p3", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
            {"title" : "p2", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
        ])
        """


class SubmitProblem(Resource):
    @jwt_required()
    def post(self):
        problem_url = request.form.get("problem_url", default="", type=str)
        code = request.form.get("code", default="", type=str)
        problem_code = getProblemCode(problem_url)
        codeforces = Codeforces()
        codeforces.login(CF_USERNAME, CF_PASSWORD)
        if codeforces.check_login():
            res = codeforces.submit(problem_code, code + "\n")
            if res["status"] == "error":
                return {"error": res["msg"]}
            else:
                return {"submissionUrl": res["msg"]}
        else:
            return {"error": "failed to submit code"}


class Submission(Resource):
    @jwt_required()
    def post(self):
        submissionUrl = request.form.get("submissionUrl", default="", type=str)
        codeforces = Codeforces()
        codeforces.login(CF_USERNAME, CF_PASSWORD)
        if codeforces.check_login():
            status = codeforces.getSubmissionStatus(submissionUrl)
            return {"status": status}
        else:
            return {"status": "failed to login"}


class GetProblem(Resource):
    @jwt_required()
    def post(self):
        problem_id = request.form.get("problem_id", default="", type=str)
        problem = getProblem(problem_id)
        return jsonify(ProblemSchema().dump(problem))


class InsertProblemToDB(Resource):
    @jwt_required()
    def get(self):
        codeforcesSpider = CodeforcesSpider()
        codeforcesSpider.start()
        return {"msg": "success"}
