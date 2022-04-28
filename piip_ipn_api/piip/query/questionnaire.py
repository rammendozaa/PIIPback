from piip.models.questionnaire import Questionnaire
from piip.services.database.setup import session


def get_questionnaires():
    return session.query(Questionnaire).filter(Questionnaire.is_active == True).all()


def get_questionnaire_by_id(questionnaire_id):
    return session.query(Questionnaire).filter(
        Questionnaire.is_active == True,
        Questionnaire.id == questionnaire_id
    ).first()
