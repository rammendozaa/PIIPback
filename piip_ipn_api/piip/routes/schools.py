from flask import jsonify
from flask_restful import Resource

from piip.command.school import get_all_schools
from piip.schema.school import SchoolSchema


class Schools(Resource):
    def get(self):
        return jsonify(SchoolSchema(many=True).dump(get_all_schools()))
