from flask_restful import Resource
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from flask import request, Flask, jsonify
from flask_restful import Resource

class LogOut(Resource):
    def post(self):
        response = jsonify({"msg": "logout successful"})
        unset_jwt_cookies(response)
        return response
