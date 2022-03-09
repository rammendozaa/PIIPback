from sqlalchemy import null
from piip.services.database.setup import session
from datetime import date
from piip.models import User


def insertUser(_firstname, _lastname, _email, _school_id, _password):
    # Check if user already exits
    user = session.query(User).filter_by(email=_email).first()
    if user:
        return 0
    new_user = User(email=_email, password=_password, dob=date.today(), first_name=_firstname, last_name=_lastname, school_id=_school_id)
    session.add(new_user)
    session.commit()
    return 1