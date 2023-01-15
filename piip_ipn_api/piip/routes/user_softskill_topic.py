from flask import request
from flask_jwt_extended import jwt_required

from piip.command.user_softskill_topic import getNumberOfSoftSkillTopicsSolved
from piip.routes.resource import PIIPResource


class GetNumberOfSoftSkillTopicsSolvedByUser(PIIPResource):
    @jwt_required()
    def post(self):
        numberOfProblems = getNumberOfSoftSkillTopicsSolved(
            request.form.get("user_id", default="", type=str)
        )
        return {"numberOfSoftSkillsTopics": numberOfProblems}
