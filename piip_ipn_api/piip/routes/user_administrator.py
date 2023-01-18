from flask import request
from flask_jwt_extended import jwt_required

from piip.command.user_administrator import (getMyStudents, getMyStudents2,
                                             getNumberOfActiveUsers,
                                             getNumberOfGraduatedStudents,
                                             getNumberOfLosers)
from piip.routes.resource import PIIPResource


class GetCurrentStudentsInterviewsData(PIIPResource):
    @jwt_required()
    def post(self):
        data = getMyStudents2(request.form.get("user_id", default="", type=str))
        return data


class GetStudentsInterviewsData(PIIPResource):
    @jwt_required()
    def post(self):
        data = getMyStudents(request.form.get("user_id", default="", type=str))
        return data


class GetNumberOfLosers(PIIPResource):
    @jwt_required()
    def post(self):
        numberOfStudents = getNumberOfLosers(
            request.form.get("user_id", default="", type=str)
        )
        return {"numberOfLosers": numberOfStudents}


class GetNumberOfGraduatedStudents(PIIPResource):
    @jwt_required()
    def post(self):
        numberOfStudents = getNumberOfGraduatedStudents(
            request.form.get("user_id", default="", type=str)
        )
        return {"numberOfGraduated": numberOfStudents}


class GetNumberOfActiveStudents(PIIPResource):
    @jwt_required()
    def post(self):
        numberOfStudents = getNumberOfActiveUsers(
            request.form.get("user_id", default="", type=str)
        )
        return {"numberOfStudents": numberOfStudents}
