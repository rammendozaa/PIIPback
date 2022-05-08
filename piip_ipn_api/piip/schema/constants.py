from piip.models import (
    Problem,
    ProgrammingTopic,
    SoftSkillQuestion,
    SoftSkillTopic,
    Interview,
    Questionnaire,
)
from piip.schema.problem import ProblemSchema
from piip.schema.topic import (
    ProgrammingTopicSchema,
    SoftSkillTopicSchema,
)
from piip.schema.question import SoftSkillQuestionSchema
from piip.schema.interview import InterviewSchema
from piip.schema.questionnaire import QuestionnaireSchema
from piip.models.user import (
    UserProblem,
    UserProgrammingTopic,
    UserQuestionnaire,
    UserSoftSkillQuestion,
    UserSoftSkillTopic,
)

ACTIVITY_TYPE_TO_SCHEMA = {
    1: ProblemSchema,
    2: ProgrammingTopicSchema,
    3: SoftSkillQuestionSchema,
    4: SoftSkillTopicSchema,
    5: InterviewSchema,
    6: QuestionnaireSchema,
}

ACTIVITY_TYPE_TO_MODEL = {
    1: Problem,
    2: ProgrammingTopic,
    3: SoftSkillQuestion,
    4: SoftSkillTopic,
    5: Interview,
    6: Questionnaire,
}

USER_ACTIVITY_TYPE_TO_MODEL = {
    1: UserProblem,
    2: UserProgrammingTopic,
    3: UserSoftSkillQuestion,
    4: UserSoftSkillTopic,
    5: Interview,
    6: UserQuestionnaire,
}