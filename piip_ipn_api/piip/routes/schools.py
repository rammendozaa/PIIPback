from flask_restful import Resource
from piip.schema.school import SchoolSchema
from flask import jsonify
from piip.command.school import get_all_schools

class Schools(Resource):
    def get(self):
        return jsonify(SchoolSchema(many=True).dump(get_all_schools()))