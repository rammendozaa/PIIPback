from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_restful import Resource
from piip.command.administrator import  assignStudent
from flask import request

class AssignStudent(Resource):
    @jwt_required()
    def post(self):
        #TODO Check role
        user_id = request.form.get("user_id", default='',type=str)
        status = assignStudent(get_jwt_identity(),user_id)
        if status == 1:
            return {"msg": "user assigned correctly"}
        return {"msg": "user is no longer available"}