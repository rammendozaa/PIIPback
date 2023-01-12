from piip.models import DictSchool
from piip.services.database.setup import session


def trying():
    school = session.query(DictSchool).get(1)
    return school
