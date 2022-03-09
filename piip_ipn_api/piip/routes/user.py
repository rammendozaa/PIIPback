from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_restful import Resource
from flask import request,jsonify
from matplotlib.pyplot import get
from piip.command.user import getMyStudents, insertUser, getAdministratorGivenUser, getUnassignedUsers, getUser
from piip.command.administrator import getAdministrator
from flask_jwt_extended import create_access_token

from piip.schema.user import UserSchema

class User(Resource):
    def post(self):
        firstname = request.form.get("firstname", default='',type=str)
        lastname = request.form.get("lastname", default='',type=str)
        email = request.form.get("email", default='',type=str)
        school_id = request.form.get("school_id", default='',type=str)
        password = request.form.get("password", default='',type=str)
                
        status = insertUser(firstname,lastname, email,school_id, password)
        if status == 0:
            return {"error": "user already exists"}
        access_token = create_access_token(identity=email)
        response = {"access_token":access_token, "role": "user"}
        return response

class GetAdministratorGivenUser(Resource):
    @jwt_required()
    def get(self):
        administrator_id = getAdministratorGivenUser(get_jwt_identity())
        return {"administrator_id": administrator_id}

class GetUnassignedUsers(Resource):
    @jwt_required()
    def get(self):
        user_ids = getUnassignedUsers()
        users = []
        for user in user_ids:
            users.append(getUser(user.user_id));
        return jsonify(UserSchema(many=True).dump(users))

class MyStudents(Resource):
    @jwt_required()
    def get(self):
        administrator = getAdministrator(get_jwt_identity())
        user_ids = getMyStudents(administrator.id)
        users = []
        for user in user_ids:
            users.append(getUser(user.user_id))
        return jsonify(UserSchema(many=True).dump(users))