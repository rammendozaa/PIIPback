from piip.routes.healthcheck import HealthCheck
from piip.routes.problem import (
    Problems,
    Submission,
    SubmitProblem,
    GetProblem,
    InsertProblemToDB
)
from piip.routes.topics import (
    GetAlgorithmsTopics,
    GetSoftSkillsTopics
)
from piip.routes.schools import Schools
from piip.routes.token import Token
from piip.routes.logout import LogOut
from piip.routes.user import (
    User,GetAdministratorGivenUser,
    GetUnassignedUsers,MyStudents,
    GetUser,
    UserTemplates,
    AddSectionToUserTemplateSection,
    AddActivityToUserTemplateActivity,
    RemoveUserTemplate,
    RemoveUserTemplateSection,
    RemoveUserTemplateActivity,
    CreateUserInterview,
)
from piip.routes.administrator import AssignStudent
from piip.routes.template import (
    Template,
    AddTemplate,
    TemplateSection,
    AddTemplateSection,
    SectionActivity,
    AddSectionActivity,
)
from piip.routes.questionnaire import Questionnaire

__all__ = [
    "LogOut",
    "Token",
    "HealthCheck",
    "Problems",
    "Submission",
    "SubmitProblem",
    "Schools",
    "User",
    "GetAdministratorGivenUser",
    "AssignStudent",
    "GetUnassignedUsers",
    "MyStudents",
    "GetProblem",
    "InsertProblemToDB",
    "GetUser",
    "Template",
    "AddTemplate",
    "TemplateSection",
    "SectionActivity",
    "AddTemplateSection",
    "AddSectionActivity",
    "UserTemplates",
    "AddSectionToUserTemplateSection",
    "AddActivityToUserTemplateActivity",
    "RemoveUserTemplate",
    "RemoveUserTemplateSection",
    "RemoveUserTemplateActivity",
    "GetAlgorithmsTopics",
    "GetSoftSkillsTopics",
    "CreateUserInterview",
    "Questionnaire",
]