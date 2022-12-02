import time
from datetime import datetime

from dateutil import tz
from flask import request
from flask_restful import Resource

from piip.command.interview import (get_interviews, getNumberOfInterviews,
                                    update_interview)
from piip.schema.interviews import InterviewSchema


class Interview(Resource):
    def put(self):
        request_json = request.get_json(silent=True) or {}
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()
        d = time.strptime(request_json["chosenDate"][:-1], "%Y-%m-%dT%H:%M:%S.%f")
        utc_str = time.strftime("%Y-%m-%d %H:%M:%S", d)
        utc = datetime.strptime(utc_str, "%Y-%m-%d %H:%M:%S")
        utc = utc.replace(tzinfo=from_zone)
        central = utc.astimezone(to_zone)
        request_json["chosenDate"] = central.strftime("%Y-%m-%d %H:%M:%S")
        interview_changes = InterviewSchema().load(request_json)
        interview_id = request.args.get("interview_id")
        user_id = request.args.get("user_id")
        role = request.args.get("role", "user")
        return {
            "updated": update_interview(user_id, interview_id, interview_changes, role)
        }

    def get(self):
        interview_id = request.args.get("interview_id", None)
        if interview_id:
            return InterviewSchema().dump(get_interviews(interview_id=interview_id))
        admin_id = request.args.get("admin_id", None)
        if admin_id:
            return InterviewSchema(many=True).dump(get_interviews(admin_id=admin_id))
        return InterviewSchema(many=True).dump(get_interviews())


class GetNumberOfInterviews(Resource):
    def post(self):
        numberOfProblems = getNumberOfInterviews(
            request.form.get("user_id", default="", type=str)
        )
        return {"ASD": 5}
