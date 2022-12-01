from piip.services.database.setup import session
from datetime import date
from piip.models import DictSchool, User


def prueba():
    school = session.query(DictSchool).get(1)
    return school