from flask import request
from flask_jwt_extended import jwt_required

from piip.command.constants import ACTIVITY_TYPES
from piip.command.ownership import mentor_only
from piip.command.template import get_all_unassigned_activities_to_section
from piip.command.topic import (create_algorithm_topic,
                                create_soft_skill_topic,
                                get_all_programming_topics,
                                get_all_softskills_topics,
                                get_all_unassigned_programming_topics,
                                get_all_unassigned_softskills_topics,
                                get_programming_topic, get_softskill_topic,
                                update_algorithm_topic,
                                update_soft_skill_topic)
from piip.models.topic import ProgrammingTopic, SoftSkillTopic
from piip.routes.resource import PIIPResource
from piip.schema.topic import ProgrammingTopicSchema, SoftSkillTopicSchema


class GetAlgorithmsTopics(PIIPResource):
    @jwt_required()
    def get(self):
        user_id = request.args.get("user_id", None)
        if user_id:
            return ProgrammingTopicSchema(many=True).dump(
                get_all_unassigned_programming_topics(user_id)
            )
        topic_id = request.args.get("topicId", None)
        if topic_id:
            return ProgrammingTopicSchema().dump(get_programming_topic(topic_id))
        section_id = request.args.get("sectionId", None)
        if section_id:
            return ProgrammingTopicSchema(many=True).dump(
                get_all_unassigned_activities_to_section(
                    section_id, ProgrammingTopic, ACTIVITY_TYPES["PROGRAMMING_TOPIC"]
                )
            )
        return ProgrammingTopicSchema(many=True).dump(get_all_programming_topics())


class GetSoftSkillsTopics(PIIPResource):
    @jwt_required()
    def get(self):
        user_id = request.args.get("user_id", None)
        if user_id:
            return SoftSkillTopicSchema(many=True).dump(
                get_all_unassigned_softskills_topics(user_id)
            )
        topic_id = request.args.get("topicId", None)
        if topic_id:
            return SoftSkillTopicSchema().dump(get_softskill_topic(topic_id))
        section_id = request.args.get("sectionId", None)
        if section_id:
            return SoftSkillTopicSchema(many=True).dump(
                get_all_unassigned_activities_to_section(
                    section_id, SoftSkillTopic, ACTIVITY_TYPES["SOFT_SKILL_TOPIC"]
                )
            )
        return SoftSkillTopicSchema(many=True).dump(get_all_softskills_topics())


class UpdateTopic(PIIPResource):
    @jwt_required()
    def post(self):
        mentor_only(request)
        request_json = request.get_json(silent=True) or {}
        topic_type = request_json.get("topicType", None)
        if not topic_type:
            return {}
        del request_json["topicType"]
        if topic_type == "SoftSkill":
            return update_soft_skill_topic(request_json)
        return update_algorithm_topic(request_json)


class CreateNewTopic(PIIPResource):
    @jwt_required()
    def post(self):
        mentor_only(request)
        request_json = request.get_json(silent=True) or {}
        topic_type = request_json.get("topicType", None)
        if not topic_type:
            return {}
        del request_json["topicType"]
        if topic_type == "SoftSkill":
            soft_skill_topic_to_add = SoftSkillTopicSchema().load(request_json)
            return SoftSkillTopicSchema().dump(
                create_soft_skill_topic(soft_skill_topic_to_add)
            )
        algorithm_topic_to_add = ProgrammingTopicSchema().load(request_json)
        return ProgrammingTopicSchema().dump(
            create_algorithm_topic(algorithm_topic_to_add)
        )
