from flask import jsonify
from flask_jwt_extended import unset_jwt_cookies
from flask_restful import Resource


class LogOut(Resource):
    def post(self):
        response = jsonify({"msg": "logout successful"})
        unset_jwt_cookies(response)
        return response
