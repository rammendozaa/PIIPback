from flask import request
from flask_jwt_extended import jwt_required

from piip.command.user_problem import (getNumberOfProblemsSolved,
                                       getNumberOfProblemsSolvedByDay,
                                       getNumberOfProblemsSolvedByTag,
                                       updateProblemStatus)
from piip.routes.resource import PIIPResource


class GetNumberOfProblemsByDay(PIIPResource):
    @jwt_required()
    def post(self):
        return getNumberOfProblemsSolvedByDay(
            request.form.get("user_id", default="", type=str)
        )


class GetNumberOfProblemsByTag(PIIPResource):
    @jwt_required()
    def post(self):
        return getNumberOfProblemsSolvedByTag(
            request.form.get("user_id", default="", type=str)
        )


class GetNumberOfProblemSolvedByUser(PIIPResource):
    @jwt_required()
    def post(self):
        numberOfProblems = getNumberOfProblemsSolved(
            request.form.get("user_id", default="", type=str)
        )
        return {"numberOfProblems": numberOfProblems}
        """
            [
            {"title" : "p1", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
            {"title" : "p3", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
            {"title" : "p2", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
        ])
        """


class UpdateProblemStatus(PIIPResource):
    @jwt_required()
    def post(self):
        problemId = request.form.get("problem_id", default="", type=str)
        userId = request.form.get("user_id", default="", type=str)
        status = request.form.get("status", default="", type=str)
        updateProblemStatus(userId, problemId, status)
        return {"status": "status updated"}
