from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from flask import request
from flask_restful import Resource
from piip.models import User,Administrator
from piip.services.database.setup import session

class Token(Resource):
    def post(self):
        _email = request.form.get("email", default='',type=str)
        _password = request.form.get("password", default='',type=str)

        user = session.query(User).filter_by(email=_email).first()
        admin = session.query(Administrator).filter_by(email=_email).first()

        if user and user.password == _password:
            access_token = create_access_token(identity=_email)
            response = {"access_token":access_token, "role": "user", "user_id": user.id}
            return response
        if admin and admin.password == _password:
            access_token = create_access_token(identity=_email)
            response = {"access_token":access_token, "role": "mentor", "user_id": admin.id}
            return response
        return {"error": "Wrong email or password"}, 401
