from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

from piip.command.administrator import assignStudent, insertAdministrator
from piip.command.ownership import mentor_only, super_only
from piip.routes.resource import PIIPResource


class AssignStudent(PIIPResource):
    @jwt_required()
    def post(self):
        mentor_only(request)
        user_id = request.form.get("user_id", default="", type=str)
        status = assignStudent(get_jwt_identity(), user_id)
        if status == 1:
            return {"msg": "user assigned correctly"}
        return {"msg": "user is no longer available"}


class AddAdministrator(PIIPResource):
    @jwt_required()
    def post(self):
        super_only(request)
        request_json = request.get_json(silent=True) or {}
        return insertAdministrator(
            request_json["name"],
            request_json["last"],
            request_json["email"],
            request_json["isSuper"],
            request_json["ps"],
        )
