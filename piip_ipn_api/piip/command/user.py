from sqlalchemy import null
from piip.services.database.setup import session
from datetime import date
from piip.models import User,UserAdministrator


def insertUser(_firstname, _lastname, _email, _school_id, _password):
    # Check if user already exits
    user = session.query(User).filter_by(email=_email).first()
    if user:
        return 0
    new_user = User(email=_email, password=_password, dob=date.today(), first_name=_firstname, last_name=_lastname, school_id=_school_id)
    session.add(new_user)
    session.commit()
    print(new_user.id)
    insertUserAdministrator(new_user)
    return 1

def insertUserAdministrator(user):
    user_administrator = UserAdministrator(user_id=user.id)
    session.add(user_administrator)
    session.commit()

def getAdministratorGivenUser(_email):
    user = session.query(User).filter_by(email=_email).first()
    _user_id = user.id
    administrator = session.query(UserAdministrator).filter_by(user_id=_user_id).first()
    if administrator.administrator_id == None:
        return -1
    return administrator.id

def getUnassignedUsers():
    users = session.query(UserAdministrator).filter_by(administrator_id=None).all()
    return users

def getMyStudents(_administrator_id):
    users = session.query(UserAdministrator).filter_by(administrator_id=_administrator_id).all()
    return users

def getUser(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    return user