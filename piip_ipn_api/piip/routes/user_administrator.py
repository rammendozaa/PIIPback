from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from piip.command.user_administrator import (getMyStudents, getMyStudents2,
                                             getNumberOfActiveUsers,
                                             getNumberOfGraduatedStudents,
                                             getNumberOfLosers)


class GetCurrentStudentsInterviewsData(Resource):
    @jwt_required()
    def post(self):
        data = getMyStudents2(request.form.get("user_id", default="", type=str))
        return data


class GetStudentsInterviewsData(Resource):
    @jwt_required()
    def post(self):
        data = getMyStudents(request.form.get("user_id", default="", type=str))
        return data


class GetNumberOfLosers(Resource):
    @jwt_required()
    def post(self):
        numberOfStudents = getNumberOfLosers(
            request.form.get("user_id", default="", type=str)
        )
        return {"numberOfLosers": numberOfStudents}


class GetNumberOfGraduatedStudents(Resource):
    @jwt_required()
    def post(self):
        numberOfStudents = getNumberOfGraduatedStudents(
            request.form.get("user_id", default="", type=str)
        )
        return {"numberOfGraduated": numberOfStudents}


class GetNumberOfActiveStudents(Resource):
    @jwt_required()
    def post(self):
        numberOfStudents = getNumberOfActiveUsers(
            request.form.get("user_id", default="", type=str)
        )
        return {"numberOfStudents": numberOfStudents}
