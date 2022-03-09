from piip.services.database.setup import session
from datetime import date
from piip.models import User


def insertUser(_firstname, _lastname, _email, _school_id, _password):
    user = User(email=_email, password=_password, dob=date.today(), first_name=_firstname, last_name=_lastname, school_id=_school_id)
    session.add(user)
    session.commit()
    return user