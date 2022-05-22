import time
from datetime import datetime
from dateutil import tz
from calendar import c
from piip.schema.template import (
    TemplateSectionSchema,
    TemplateActivitySchema,
)
from piip.command.template import (
    add_template_section,
    add_section_activity,
)
from piip.command.company_tracking import (
    get_company_tracking_for_user,
    create_company_tracking_for_user,
    create_company_tracking_link,
    delete_company_tracking_link,
    delete_company_tracking,
    update_company_tracking_link,
    update_company_tracking,
)
from piip.command.user import create_user_interview
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_restful import Resource
from flask import request,jsonify
from piip.command.user import getMyStudents, insertUser, getAdministratorGivenUser, getUnassignedUsers, getUser
from piip.command.administrator import getAdministrator
from flask_jwt_extended import create_access_token
from piip.schema.user import UserSchema
from piip.command.user import (
    assign_template_to_user_id,
    assign_template_section_to_user_id,
    assign_template_activity_to_user_id,
    get_active_user_templates,
    disable_user_template_by_id,
    disable_user_template_section_by_id,
    disable_user_template_activity_by_id,
    register_first_user_questionnaire,
    create_initial_user_questionnaire,
    grade_questionnaire,
    update_user_topic,
    update_user_soft_skill_question,
)
from piip.schema.user import (
    UserTemplateSchema,
    UserTemplateSectionSchema,
    UserTemplateActivitySchema,
)
from piip.query.user import (
    get_user_template_section_by_id,
    update_user_template_activity_by_id,
)
from piip.command.constants import ACTIVITY_TYPES
from piip.schema.company_tracking import (
    CompanyTrackingSchema,
    CompanyTrackingLinksSchema,
)

class User(Resource):
    def post(self):
        firstname = request.form.get("firstname", default='',type=str)
        lastname = request.form.get("lastname", default='',type=str)
        email = request.form.get("email", default='',type=str)
        school_id = request.form.get("school_id", default='',type=str)
        password = request.form.get("password", default='',type=str)
                
        user_id = insertUser(firstname,lastname, email,school_id, password)
        if user_id == -1:
            return {"error": "user already exists"}
        access_token = create_access_token(identity=email)
        create_initial_user_questionnaire(user_id)
        response = {"access_token":access_token, "role": "user", "user_id": user_id}
        return response

class GetAdministratorGivenUser(Resource):
    @jwt_required()
    def get(self):
        administrator_id = getAdministratorGivenUser(get_jwt_identity())
        return {"administrator_id": administrator_id}

class GetUnassignedUsers(Resource):
    @jwt_required()
    def get(self):
        user_ids = getUnassignedUsers()
        users = []
        for user in user_ids:
            users.append(user.user)
        return jsonify(UserSchema(many=True).dump(users))

class MyStudents(Resource):
    @jwt_required()
    def get(self):
        administrator = getAdministrator(get_jwt_identity())
        user_ids = getMyStudents(administrator.id)
        users = []
        for user in user_ids:
            users.append(user.user)
        return jsonify(UserSchema(many=True).dump(users))

class GetUser(Resource):
    @jwt_required()
    def get(self):
        user = getUser(get_jwt_identity())
        return jsonify(UserSchema().dump(user))


class UserTemplates(Resource):
    def post(self, user_id: int):
        template_dict = request.get_json() or {}
        template_ids = template_dict["templateIds"]
        assign_template_to_user_id(user_id, template_ids)
        return UserTemplateSchema().dump(get_active_user_templates(user_id))

    def get(self, user_id: int):
        return UserTemplateSchema().dump(get_active_user_templates(user_id))


class AddSectionToUserTemplateSection(Resource):
    def post(self, user_id: int, user_template_id: int):
        create_section = TemplateSectionSchema().load(
            request.get_json(silent=True) or {}
            )
        template_section = add_template_section(None, create_section)
        return (
            UserTemplateSectionSchema().dump(
                assign_template_section_to_user_id(user_id, template_section, user_template_id)
            )
        )


class AddActivityToUserTemplateActivity(Resource):
    def post(self, user_id: int, user_template_section_id: int):
        request_json = request.get_json(silent=True) or {}
        create_activity = TemplateActivitySchema().load(
            request_json
        )
        user_admin_id = None
        user_template_section = get_user_template_section_by_id(user_template_section_id)
        template_activity = add_section_activity(user_template_section.template_section_id, create_activity)
        if (create_activity.activity_type_id == ACTIVITY_TYPES["INTERVIEW"]):
            user_admin_id = request_json.get("userAdminId", None)
        return (
            UserTemplateActivitySchema().dump(
                assign_template_activity_to_user_id(
                    user_id,
                    template_activity,
                    user_template_section_id,
                )
            )
        )


class RemoveUserTemplate(Resource):
    def delete(self, user_template_id: int):
        return UserTemplateSchema().dump(
            disable_user_template_by_id(user_template_id)
        )


class RemoveUserTemplateSection(Resource):
    def delete(self, user_template_section_id: int):
        return UserTemplateSectionSchema().dump(
            disable_user_template_section_by_id(user_template_section_id)
        )


class CreateUserInterview(Resource):
    def post(self, user_id: int, user_template_section_id: int):
        request_json = request.get_json(silent=True) or {}
        user_interview = create_user_interview(user_id, request_json.get("userAdminId"), request_json.get("interviewType", 1), request_json.get("description", None))
        request_json["externalReference"] = user_interview.id
        del request_json["userAdminId"]
        interview_type = request_json.get("interviewType", None)
        if interview_type:
            del request_json["interviewType"]
        create_activity = TemplateActivitySchema().load(
            request_json
        )
        user_template_section = get_user_template_section_by_id(user_template_section_id)
        template_activity = add_section_activity(user_template_section.template_section_id, create_activity)
        return (
            UserTemplateActivitySchema().dump(
                assign_template_activity_to_user_id(
                    user_id,
                    template_activity,
                    user_template_section_id,
                )
            )
        )


class RegisterUserQuestionnaire(Resource):
    def put(self, user_id: int, questionnaire_id: int):
        request_json = request.get_json(silent=True) or {}
        questionnaire = register_first_user_questionnaire(user_id, questionnaire_id, request_json["correctAnswers"])
        return {"registered": (questionnaire is not None)}


class UpdateUserTemplateActivity(Resource):
    def put(self, user_template_activity_id: int):
        request_json = request.get_json(silent=True) or {}
        return {
            "updated": update_user_template_activity_by_id(
                user_template_activity_id, request_json.get("statusId", 1)
                )
            }
    def delete(self, user_template_activity_id: int):
        return UserTemplateActivitySchema().dump(
            disable_user_template_activity_by_id(user_template_activity_id)
        )


class UpdateUserQuestionnaire(Resource):
    def put(self, user_id: int, questionnaire_id: int):
        request_json = request.get_json(silent=True) or {}
        questionnaire = grade_questionnaire(user_id, questionnaire_id, request_json["correctAnswers"])
        return {"registered": (questionnaire is not None)}


class UpdateUserTopic(Resource):
    def put(self, user_id: int, topic_type: str, topic_id: int):
        request_json = request.get_json(silent=True) or {}
        return {
            "updated": update_user_topic(user_id, topic_type, topic_id, request_json.get("statusId", 1))
        }


class UpdateUserSoftSkillQuestion(Resource):
    def put(self, user_id:int, question_id:int):
        request_json = request.get_json(silent=True) or {}
        return {
            "updated": update_user_soft_skill_question(
                user_id,
                question_id,
                request_json.get("answer", ""),
                request_json.get("statusId", 1),
            )
        }

def get_local_date(utc_date):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    d = time.strptime(utc_date[:-1], "%Y-%m-%dT%H:%M:%S.%f")
    utc_str = time.strftime("%Y-%m-%d %H:%M:%S", d)
    utc = datetime.strptime(utc_str, '%Y-%m-%d %H:%M:%S')
    utc = utc.replace(tzinfo=from_zone)
    central = utc.astimezone(to_zone)
    return central.strftime("%Y-%m-%d %H:%M:%S")

class UserCompanyTracking(Resource):
    def get(self, user_id: int):
        return CompanyTrackingSchema(many=True).dump(
            get_company_tracking_for_user(user_id)
        )

    def post(self, user_id: int):
        request_json = request.get_json(silent=True) or {}
        request_json["userId"] = user_id
        interview_date = request_json.get("interviewDate", None)
        if interview_date:
            request_json["interviewDate"] = get_local_date(interview_date)
        company_tracking = CompanyTrackingSchema().load(request_json)
        return CompanyTrackingSchema().dump(
            create_company_tracking_for_user(company_tracking)
        )


class CompanyTrackingLink(Resource):
    def delete(self, company_tracking_link_id: int):
        return {"deleted": delete_company_tracking_link(company_tracking_link_id)}

    def put(self, company_tracking_link_id: int):
        request_json = request.get_json(silent=True) or {}
        company_tracking_link = CompanyTrackingLinksSchema().load(request_json)
        return {"updated": update_company_tracking_link(company_tracking_link_id, company_tracking_link)}


class CompanyTracking(Resource):
    def post(self, company_tracking_id: int):
        request_json = request.get_json(silent=True) or {}
        request_json["companyTrackingId"] = company_tracking_id
        company_tracking_link = CompanyTrackingLinksSchema().load(request_json)
        return CompanyTrackingLinksSchema().dump(
            create_company_tracking_link(company_tracking_link)
        )
    
    def delete(self, company_tracking_id: int):
        return {"deleted": delete_company_tracking(company_tracking_id)}

    def put(self, company_tracking_id: int):
        request_json = request.get_json(silent=True) or {}
        interview_date = request_json.get("interviewDate", None)
        if interview_date:
            request_json["interviewDate"] = get_local_date(interview_date)
        company_tracking = CompanyTrackingSchema().load(request_json)
        return {"updated": update_company_tracking(company_tracking_id, company_tracking)}
