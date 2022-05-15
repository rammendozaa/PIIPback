from piip.routes.healthcheck import HealthCheck
from piip.routes.problem import (
    Problems,
    Submission,
    SubmitProblem,
    GetProblem,
    InsertProblemToDB,
    GetRecommendations
)
from piip.routes.user_administrator import (
    GetNumberOfActiveStudents,
    GetNumberOfGraduatedStudents,
    GetNumberOfLosers,
    GetStudentsInterviewsData,
    GetCurrentStudentsInterviewsData
)
from piip.routes.user_problem import (
    GetNumberOfProblemSolvedByUser,
    GetNumberOfProblemsByTag,
    GetNumberOfProblemsByDay,
    UpdateProblemStatus
)
from piip.routes.user_programming_topic import (
    GetNumberOfProgrammingTopicsSolvedByUser
)
from piip.routes.user_softskill_topic import (
    GetNumberOfSoftSkillTopicsSolvedByUser
)
from piip.routes.interview import (
    Interview,
    GetNumberOfInterviews
)
from piip.routes.topics import (
    GetAlgorithmsTopics,
    GetSoftSkillsTopics,
    CreateNewTopic,
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
    RegisterUserQuestionnaire,
    UpdateUserTemplateActivity,
    UpdateUserQuestionnaire,
    UpdateUserTopic,
    UpdateUserSoftSkillQuestion,
    UserCompanyTracking,
    CompanyTrackingLink,
    CompanyTracking,
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
from piip.routes.soft_skills import SoftSkillQuestion


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
    "UpdateProblemStatus",
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
    "RegisterUserQuestionnaire",
    "Questionnaire",
    "UpdateUserTemplateActivity",
    "CreateNewTopic",
    "GetCurrentStudentsInterviewsData",
    "GetStudentsInterviewsData",
    "GetNumberOfActiveStudents",
    "GetNumberOfGraduatedStudents",
    "GetNumberOfLosers",
    "GetRecommendations",
    "GetNumberOfProblemsByDay",
    "GetNumberOfProblemsByTag",
    "GetNumberOfProblemSolvedByUser",
    "GetNumberOfProgrammingTopicsSolvedByUser",
    "GetNumberOfSoftSkillTopicsSolvedByUser",
    "GetNumberOfInterviews",
    "SoftSkillQuestion",
    "UpdateUserQuestionnaire",
    "UpdateUserTopic",
    "UpdateUserSoftSkillQuestion",
    "Interview",
    "UserCompanyTracking",
    "CompanyTrackingLink",
    "CompanyTracking",
]