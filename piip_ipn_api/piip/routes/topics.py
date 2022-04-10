from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from piip.schema.topic import ProgrammingTopicSchema, SoftSkillTopicSchema
from piip.command.topic import get_all_programming_topics, get_all_softskills_topics

class GetAlgorithmsTopics(Resource):
    @jwt_required()
    def get(self):
        return jsonify(ProgrammingTopicSchema(many=True).dump(get_all_programming_topics()))

class GetSoftSkillsTopics(Resource):
    @jwt_required()
    def get(self):
        return jsonify(SoftSkillTopicSchema(many=True).dump(get_all_softskills_topics()))