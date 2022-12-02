from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource

from piip.models import Administrator, User
from piip.services.database.setup import session
from piip.validate_password import is_correct_password


class Token(Resource):
    def post(self):
        _email = request.form.get("email", default="", type=str)
        _password = request.form.get("password", default="", type=str)

        user = session.query(User).filter_by(email=_email).first()
        if user:
            if is_correct_password(user.salt, user.hash, _password):
                access_token = create_access_token(identity=_email)
                response = {
                    "access_token": access_token,
                    "role": "user",
                    "user_id": user.id,
                }
                return response
        admin = session.query(Administrator).filter_by(email=_email).first()
        if admin:
            if is_correct_password(admin.salt, admin.hash, _password):
                access_token = create_access_token(identity=_email)
                if admin.is_super == 1:
                    response = {
                        "access_token": access_token,
                        "role": "super",
                        "user_id": admin.id,
                    }
                else:
                    response = {
                        "access_token": access_token,
                        "role": "mentor",
                        "user_id": admin.id,
                    }
                return response
        return {"error": "Wrong email or password"}, 401
