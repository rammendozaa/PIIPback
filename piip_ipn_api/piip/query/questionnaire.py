from piip.models.questionnaire import Questionnaire
from piip.services.database.setup import session


def get_questionnaires():
    return session.query(Questionnaire).filter(Questionnaire.is_active == True).all()
