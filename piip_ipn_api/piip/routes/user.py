from flask_restful import Resource
from flask import request
from piip.command.user import insertUser
from flask_jwt_extended import create_access_token

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