from piip.services.database.setup import session
from piip.models.user import (
    User,
    UserTemplate,
    UserTemplateSection,
    UserTemplateActivity,
    UserSoftSkillQuestion,
    UserProblem,
    UserQuestionnaire,
)
from piip.schema.base_schema import BaseSchema
from marshmallow import fields, post_dump
from marshmallow.utils import EXCLUDE
from piip.schema.template import (
    TemplateSchema,
    TemplateActivitySchema,
    TemplateSectionSchema,
)
from piip.models.user import UserProgrammingTopic, UserSoftSkillTopic

class UserSchema(BaseSchema):
    __model__ = User

    id = fields.String(data_key="id") 
    email = fields.String(data_key="email")
    first_name = fields.String(data_key="first_name")
    last_name = fields.String(data_key="last_name")
    school_id = fields.String(data_key="school_id")
    is_active = fields.Integer(data_key="is_active")

# ACTIVITIES
class UserProblemSchema(BaseSchema):
    __model__ = UserProblem

    id = fields.Integer(data_key='id')
    user_id = fields.String(data_key='user_id')
    problem_id = fields.String(data_key="problem_id")
    status_id = fields.Integer(data_key="status_id")
    finished_date = fields.String(data_key="finished_date")
    code = fields.String()

class UserProgrammingTopicSchema(BaseSchema):
    __model__ = UserProgrammingTopic
    
    id = fields.Integer()
    status_id = fields.Integer()


class UserSoftSkillQuestionSchema(BaseSchema):
    __model__ = UserSoftSkillQuestion

    id = fields.Integer()
    answer = fields.String()


class UserSoftSkillTopicSchema(BaseSchema):
    __model__ = UserSoftSkillTopic

    id = fields.Integer()
    status_id = fields.Integer()


class UserQuestionnaireSchema(BaseSchema):
    __model__ = UserQuestionnaire
    
    id = fields.Integer()
    status_id = fields.Integer()
    correct_answers = fields.Integer()
    percentage_score = fields.Float()

USER_ACTIVITY_TYPE_TO_SCHEMA = {
    1: UserProblemSchema,
    2: UserProgrammingTopicSchema,
    3: UserSoftSkillQuestionSchema,
    4: UserSoftSkillTopicSchema,
    6: UserQuestionnaireSchema,
}

# TEMPLATES
class UserTemplateActivitySchema(BaseSchema):
    __model__ = UserTemplateActivity

    id = fields.Integer()
    user_id = fields.Integer()
    template_activity = fields.Nested(TemplateActivitySchema)
    status_id = fields.Integer()
    position = fields.Integer()
    finished_date = fields.String()
    external_reference = fields.Integer()

    @post_dump
    def after_serialize(self, data, many, **kwargs):
        activity_type = data["template_activity"]["activityType"]
        external_reference = data["external_reference"]
        activity = None
        activity_schema = USER_ACTIVITY_TYPE_TO_SCHEMA.get(activity_type, None)
        if activity_type == 1:
            activity = (
                session.query(UserProblem)
                .filter(
                    UserProblem.user_id == data["user_id"],
                    UserProblem.problem_id == external_reference
                )
                .first()
            )
        elif activity_type == 2:
            activity = (
                session.query(UserProgrammingTopic)
                .filter(
                    UserProgrammingTopic.user_id == data["user_id"],
                    UserProgrammingTopic.programming_topic_id == external_reference
                )
                .first()
            )
        elif activity_type == 3:
            activity = (
                session.query(UserSoftSkillQuestion)
                .filter(
                    UserSoftSkillQuestion.user_id == data["user_id"],
                    UserSoftSkillQuestion.question_id == external_reference
                )
                .first()
            )
        elif activity_type == 4:
            activity = (
                session.query(UserSoftSkillTopic)
                .filter(
                    UserSoftSkillTopic.user_id == data["user_id"],
                    UserSoftSkillTopic.soft_skill_topic_id == external_reference
                )
                .first()
            )
        elif activity_type == 6:
            activity = (
                session.query(UserQuestionnaire)
                .filter(
                    UserQuestionnaire.user_id == data["user_id"],
                    UserQuestionnaire.questionnaire_id == external_reference
                )
                .first()
            )
        
        if activity and activity_schema:
            data["activity_progress"] = activity_schema().dump(activity)
        else:
            data["activity_progress"] = None
        return data


class UserTemplateSectionSchema(BaseSchema):
    __model__ = UserTemplateSection

    id = fields.Integer()
    template_section = fields.Nested(TemplateSectionSchema)
    status_id = fields.Integer()
    position = fields.Integer()

    user_activities = fields.List(fields.Nested(
        UserTemplateActivitySchema
    ))
    @post_dump
    def after_serialize(self, data, many, **kwargs):
        template_section = data.get("template_section", None)
        if (template_section):
            del data["template_section"]["activities"]
        return data


class UserTemplateSchema(BaseSchema):
    __model__ = UserTemplate

    id = fields.Integer()
    template = fields.Nested(TemplateSchema)
    status_id = fields.Integer()
    position = fields.Integer()

    user_sections = fields.List(fields.Nested(
        UserTemplateSectionSchema
    ))
    @post_dump
    def after_serialize(self, data, many, **kwargs):
        template = data.get("template", None)
        if (template):
            del data["template"]["sections"]
        return data
