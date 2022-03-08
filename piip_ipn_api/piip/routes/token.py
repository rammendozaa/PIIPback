from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from flask import request, Flask, jsonify
from flask_restful import Resource
from piip.models.user import User


class Token(Resource):
    def post(self):
        email = request.form.get("email", default='',type=str)
        password = request.form.get("password", default='',type=str)

        if email == "hugo" and password == "hugo":
            access_token = create_access_token(identity=email)
            response = {"access_token":access_token, "role": "mentor"}
            
            user = User(username="test", roles=["foo", "bar"])

            return response
        if email == "alvaro" and password == "alvaro":
            access_token = create_access_token(identity=email)
            response = {"access_token":access_token, "role": "user"}
            return response
        return {"msg": "Wrong email or password"}, 401
