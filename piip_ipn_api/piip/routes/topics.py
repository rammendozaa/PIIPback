from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from piip.schema.topic import ProgrammingTopicSchema, SoftSkillTopicSchema
from piip.command.topic import (
    get_all_programming_topics,
    get_all_softskills_topics,
    create_soft_skill_topic,
    create_algorithm_topic,
    get_programming_topic,
    get_softskill_topic,
)

class GetAlgorithmsTopics(Resource):
    def get(self):
        topic_id = request.args.get("topicId", None)
        if topic_id:
            return ProgrammingTopicSchema().dump(get_programming_topic(topic_id))
        return jsonify(ProgrammingTopicSchema(many=True).dump(get_all_programming_topics()))


class GetSoftSkillsTopics(Resource):
    def get(self):
        topic_id = request.args.get("topicId", None)
        if topic_id:
            return SoftSkillTopicSchema().dump(get_softskill_topic(topic_id))
        return jsonify(SoftSkillTopicSchema(many=True).dump(get_all_softskills_topics()))


class CreateNewTopic(Resource):
    def post(self):
        request_json = request.get_json(silent=True) or {}
        topic_type = request_json.get("topicType", None)
        if not topic_type:
            return {}
        del request_json["topicType"]
        if topic_type == "SoftSkill":
            soft_skill_topic_to_add = SoftSkillTopicSchema().load(request_json)
            return SoftSkillTopicSchema().dump(create_soft_skill_topic(soft_skill_topic_to_add))
        algorithm_topic_to_add = ProgrammingTopicSchema().load(request_json)
        return ProgrammingTopicSchema().dump(create_algorithm_topic(algorithm_topic_to_add))
