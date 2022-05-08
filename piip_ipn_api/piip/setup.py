from ast import Assign
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from flask import Flask
from flask import Response
from datetime import datetime, timedelta, timezone
import json
from flask_restful import Api
from piip.routes.healthcheck import HealthCheck
from piip.routes import (
    LogOut,
    Token,
    HealthCheck,
    Problems,
    SubmitProblem,
    Submission,
    Schools,
    User,
    GetAdministratorGivenUser,
    AssignStudent,
    GetUnassignedUsers,
    MyStudents,
    GetProblem,
    InsertProblemToDB,
    GetNumberOfProblemSolvedByUser,
    GetNumberOfProgrammingTopicsSolvedByUser,
    GetNumberOfSoftSkillTopicsSolvedByUser,
    GetUser,
    Template,
    AddTemplate,
    TemplateSection,
    AddTemplateSection,
    SectionActivity,
    AddSectionActivity,
    UserTemplates,
    AddSectionToUserTemplateSection,
    AddActivityToUserTemplateActivity,
    RemoveUserTemplate,
    RemoveUserTemplateSection,
    RemoveUserTemplateActivity,
    GetAlgorithmsTopics,
    GetSoftSkillsTopics,
    CreateUserInterview,
    Questionnaire,
    RegisterUserQuestionnaire,
    UpdateUserTemplateActivity,
    CreateNewTopic,
    SoftSkillQuestion,
    UpdateUserQuestionnaire,
    UpdateUserTopic,
    UpdateUserSoftSkillQuestion,
    Interview,
)
from piip.services.database.setup import session
from piip.constants import (
    USERNAME,
    PASSWORD,
    HOST,
    DATABASE
)
#piipipn2021@gmail.com
#piip_ipn
#*&WcgpYU4-.{mt.-

def create_application(name):

    class localFlask(Flask):
        def process_response(self, response):
            response.headers["Access-Control-Allow-Origin"] = "*"
            response.headers["Access-Control-Allow-Credentials"] =  True
            response.headers["Access-Control-Allow-Methods"] =  "GET,HEAD,OPTIONS,POST,PUT, DELETE"
            response.headers["Access-Control-Allow-Headers"] =  "Authorization, Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"
            return (response)

    app = localFlask(name)
    app.config["JWT_SECRET_KEY"] = "please-remember-to-change-me"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

    jwt = JWTManager(app)

    app.config['JSON_SORT_KEYS'] = False

    database_route = f"mysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
    app.config["SQLALCHEMY_DATABASE_URI"] = database_route

    @app.after_request
    def refresh_expiring_jwts(response):
        try:
            exp_timestamp = get_jwt()["exp"]
            now = datetime.now(timezone.utc)
            target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
            if target_timestamp > exp_timestamp:
                access_token = create_access_token(identity=get_jwt_identity())
                data = response.get_json()
                if type(data) is dict:
                    data["access_token"] = access_token 
                    response.data = json.dumps(data)
            return response
        except (RuntimeError, KeyError):
            # Case where there is not a valid JWT. Just return the original respone
            return response

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        session.remove()

    api = Api(app)
    api.add_resource(HealthCheck, "/")

    api.add_resource(Problems, "/problems")
    api.add_resource(GetProblem,"/problem")
    api.add_resource(SubmitProblem, "/problem/submit")    
    api.add_resource(Submission, "/submission")
    api.add_resource(InsertProblemToDB,"/insertProblemsToDB")

    api.add_resource(GetNumberOfProblemSolvedByUser,"/getNumberOfProblemsSolvedByUser")
    api.add_resource(GetNumberOfProgrammingTopicsSolvedByUser,"/getNumberOfProgrammingTopicsSolvedByUser")
    api.add_resource(GetNumberOfSoftSkillTopicsSolvedByUser,"/getNumberOfSoftSkillTopicsSolvedByUser")

    api.add_resource(GetAlgorithmsTopics,"/algorithmTopics")
    api.add_resource(GetSoftSkillsTopics,"/softSkillsTopics")

    api.add_resource(Token, "/token")
    api.add_resource(LogOut, "/logout")
    api.add_resource(User, "/sign-up")
    api.add_resource(GetUser, "/user")
    api.add_resource(GetAdministratorGivenUser,"/get-admin")
    api.add_resource(GetUnassignedUsers,"/pendingStudents")
    api.add_resource(MyStudents,"/myStudents")

    api.add_resource(AssignStudent,"/assign-student")

    api.add_resource(Schools, "/schools")

    api.add_resource(Template, "/template/<int:template_id>")
    api.add_resource(TemplateSection, "/template/section/<int:section_id>")
    api.add_resource(SectionActivity, "/template/section/activity/<int:activity_id>")

    api.add_resource(AddTemplate, "/template/add")
    api.add_resource(AddTemplateSection, "/template/<int:template_id>/section/add")
    api.add_resource(AddSectionActivity, "/activity/section/<int:section_id>/activity/add")

    api.add_resource(UserTemplates, "/user/<int:user_id>/template")
    api.add_resource(AddSectionToUserTemplateSection, "/user/<int:user_id>/section/<int:user_template_id>")
    api.add_resource(AddActivityToUserTemplateActivity, "/user/<int:user_id>/activity/<int:user_template_section_id>")
    api.add_resource(RemoveUserTemplate, "/user/template/<int:user_template_id>/delete")
    api.add_resource(RemoveUserTemplateSection, "/user/section/<int:user_template_section_id>/delete")
    api.add_resource(RemoveUserTemplateActivity, "/user/activity/<int:user_template_activity_id>/delete")
    api.add_resource(RegisterUserQuestionnaire, "/user/<int:user_id>/questionnaire/<int:questionnaire_id>/assign")
    api.add_resource(UpdateUserTemplateActivity, "/user/activity/<int:user_template_activity_id>")

    api.add_resource(CreateUserInterview, "/user/<int:user_id>/interview/<int:user_template_section_id>")
    api.add_resource(Questionnaire, "/questionnaire")
    api.add_resource(SoftSkillQuestion, "/soft-skill-question")
    api.add_resource(CreateNewTopic, "/create-topic")

    api.add_resource(UpdateUserQuestionnaire, "/user/<int:user_id>/questionnaire/<int:questionnaire_id>")
    api.add_resource(UpdateUserTopic, "/user/<int:user_id>/topic/<string:topic_type>/<int:topic_id>")
    api.add_resource(UpdateUserSoftSkillQuestion, "/user/<int:user_id>/soft-skill-question/<int:question_id>")
    api.add_resource(Interview, "/interview")

    return app
