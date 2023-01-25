from piip.routes.administrator import AddAdministrator, AssignStudent
from piip.routes.healthcheck import HealthCheck
from piip.routes.interview import GetNumberOfInterviews, Interview
from piip.routes.logout import LogOut
from piip.routes.problem import (GetProblem, GetRecommendations,
                                 InsertProblemToDB, Problems, Submission,
                                 SubmitProblem)
from piip.routes.questionnaire import QuestionnaireRoute
from piip.routes.schools import Schools
from piip.routes.soft_skills import SoftSkillQuestionRoute
from piip.routes.template import (AddSectionActivity, AddTemplate,
                                  AddTemplateSection, SectionActivity,
                                  Template, TemplateSection)
from piip.routes.token import Token
from piip.routes.topics import (CreateNewTopic, GetAlgorithmsTopics,
                                GetSoftSkillsTopics, UpdateTopic)
from piip.routes.user import (AddActivityToUserTemplateActivity,
                              AddSectionToUserTemplateSection, CompanyTracking,
                              CompanyTrackingLink, ConfirmEmail,
                              CreateUserInterview, GetAdministratorGivenUser,
                              GetUnassignedUsers, GetUser, MyStudents, SendConfirmationEmail,
                              RegisterUserQuestionnaire, RemoveUserTemplate,
                              RemoveUserTemplateSection,
                              UpdateUserQuestionnaire,
                              UpdateUserSoftSkillQuestion,
                              UpdateUserTemplateActivity, UpdateUserTopic,
                              User, UserCompanyTracking, UserTemplates)
from piip.routes.user_administrator import (GetCurrentStudentsInterviewsData,
                                            GetNumberOfActiveStudents,
                                            GetNumberOfGraduatedStudents,
                                            GetNumberOfLosers,
                                            GetStudentsInterviewsData)
from piip.routes.user_problem import (GetNumberOfProblemsByDay,
                                      GetNumberOfProblemsByTag,
                                      GetNumberOfProblemSolvedByUser,
                                      UpdateProblemStatus)
from piip.routes.user_programming_topic import \
    GetNumberOfProgrammingTopicsSolvedByUser
from piip.routes.user_softskill_topic import \
    GetNumberOfSoftSkillTopicsSolvedByUser

__all__ = [
    "LogOut",
    "Token",
    "HealthCheck",
    "Problems",
    "Submission",
    "SubmitProblem",
    "Schools",
    "User",
    "ConfirmEmail",
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
    "GetAlgorithmsTopics",
    "GetSoftSkillsTopics",
    "CreateUserInterview",
    "RegisterUserQuestionnaire",
    "QuestionnaireRoute",
    "UpdateUserTemplateActivity",
    "CreateNewTopic",
    "UpdateTopic",
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
    "SendConfirmationEmail",
    "SoftSkillQuestionRoute",
    "UpdateUserQuestionnaire",
    "UpdateUserTopic",
    "UpdateUserSoftSkillQuestion",
    "Interview",
    "UserCompanyTracking",
    "CompanyTrackingLink",
    "CompanyTracking",
    "AddAdministrator",
]
