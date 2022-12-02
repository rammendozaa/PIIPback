from piip.models.questionnaire import Questionnaire
from piip.models.user import UserQuestionnaire
from piip.services.database.setup import session


def get_questionnaires():
    return session.query(Questionnaire).filter(Questionnaire.is_active == True).all()


def get_questionnaire_by_id(questionnaire_id):
    return (
        session.query(Questionnaire)
        .filter(Questionnaire.is_active == True, Questionnaire.id == questionnaire_id)
        .first()
    )


def get_unassigned_questionnaires(user_id):
    questionnaires = (
        session.query(UserQuestionnaire.questionnaire_id)
        .filter(
            UserQuestionnaire.user_id == user_id, UserQuestionnaire.is_active == True
        )
        .all()
    )
    questionnaire_list = [quiz[0] for quiz in questionnaires]
    return (
        session.query(Questionnaire)
        .filter(Questionnaire.id.notin_(questionnaire_list))
        .all()
    )
