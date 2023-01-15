from flask import Response
from flask_jwt_extended import unset_jwt_cookies

from piip.routes.resource import PIIPResource


class LogOut(PIIPResource):
    def post(self):
        response_message = {"msg": "logout successful"}
        response = Response(response_message)
        unset_jwt_cookies(response)
        return response_message
