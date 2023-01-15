from flask import request
from flask_jwt_extended import jwt_required

from piip.command.constants import ACTIVITY_TYPES
from piip.command.ownership import mentor_only, user_only
from piip.command.problem import (get_all_problems,
                                  get_all_unassigned_problems, getProblem,
                                  getProblemCode, getRecommendations)
from piip.command.template import get_all_unassigned_activities_to_section
from piip.models.problem import Problem
from piip.routes.resource import PIIPResource
from piip.schema.problem import ProblemSchema
from piip.services.providers.codeforces.codeforces import Codeforces
from piip.services.providers.codeforces.codeforcesCrawler import \
    CodeforcesSpider

CF_USERNAME = "piip_ipn"
CF_PASSWORD = "*&WcgpYU4-.{mt.-"


class GetRecommendations(PIIPResource):
    @jwt_required()
    def post(self):
        return ProblemSchema(many=True).dump(getRecommendations())


class Problems(PIIPResource):
    @jwt_required()
    def get(self):
        user_id = request.args.get("user_id", None)
        if user_id:
            return ProblemSchema(many=True).dump(get_all_unassigned_problems(user_id))
        section_id = request.args.get("sectionId", None)
        if section_id:
            return ProblemSchema(many=True).dump(
                get_all_unassigned_activities_to_section(
                    section_id, Problem, ACTIVITY_TYPES["PROBLEM"]
                )
            )
        return ProblemSchema(many=True).dump(get_all_problems())
        """
            [
            {"title" : "p1", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
            {"title" : "p3", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
            {"title" : "p2", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
        ])
        """


class SubmitProblem(PIIPResource):
    @jwt_required()
    def post(self):
        user_only(request)
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


class Submission(PIIPResource):
    @jwt_required()
    def post(self):
        user_only(request)
        submissionUrl = request.form.get("submissionUrl", default="", type=str)
        codeforces = Codeforces()
        codeforces.login(CF_USERNAME, CF_PASSWORD)
        if codeforces.check_login():
            status = codeforces.getSubmissionStatus(submissionUrl)
            return {"status": status}
        else:
            return {"status": "failed to login"}


class GetProblem(PIIPResource):
    @jwt_required()
    def post(self):
        problem_id = request.form.get("problem_id", default="", type=str)
        return ProblemSchema().dump(getProblem(problem_id))


class InsertProblemToDB(PIIPResource):
    @jwt_required()
    def get(self):
        mentor_only(request)
        codeforcesSpider = CodeforcesSpider()
        codeforcesSpider.start()
        return {"msg": "success"}
