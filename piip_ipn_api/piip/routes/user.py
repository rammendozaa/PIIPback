from piip.schema.template import (
    TemplateSectionSchema,
    TemplateActivitySchema,
)
from piip.command.template import (
    add_template_section,
    add_section_activity,
)
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
)
from piip.schema.user import (
    UserTemplateSchema,
    UserTemplateSectionSchema,
    UserTemplateActivitySchema,
)
from piip.query.user import get_user_template_section_by_id


class User(Resource):
    def post(self):
        firstname = request.form.get("firstname", default='',type=str)
        lastname = request.form.get("lastname", default='',type=str)
        email = request.form.get("email", default='',type=str)
        school_id = request.form.get("school_id", default='',type=str)
        password = request.form.get("password", default='',type=str)
                
        status = insertUser(firstname,lastname, email,school_id, password)
        if status == 0:
            return {"error": "user already exists"}
        access_token = create_access_token(identity=email)
        response = {"access_token":access_token, "role": "user"}
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
        return UserTemplateSchema(many=True).dump(get_active_user_templates(user_id))

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
        create_activity = TemplateActivitySchema().load(
            request.get_json(silent=True) or {}
        )
        user_template_section = get_user_template_section_by_id(user_template_section_id)
        template_activity = add_section_activity(user_template_section.template_section_id, create_activity)
        return (
            UserTemplateActivitySchema().dump(
                assign_template_activity_to_user_id(user_id, template_activity, user_template_section_id)
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


class RemoveUserTemplateActivity(Resource):
    def delete(self, user_template_activity_id: int):
        return UserTemplateActivitySchema().dump(
            disable_user_template_activity_by_id(user_template_activity_id)
        )
