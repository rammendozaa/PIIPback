from piip.models import DictSchool
from piip.services.database.setup import session

def get_all_schools():
    return session.query(DictSchool).all()
