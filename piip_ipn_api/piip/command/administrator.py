from datetime import date

from piip.models import Administrator, UserAdministrator
from piip.services.database.setup import session
from piip.validate_password import hash_new_password


def assignStudent(_email, _user_id):
    administrator = session.query(Administrator).filter_by(email=_email).first()
    administrator_id = administrator.id

    userAdministrator = (
        session.query(UserAdministrator).filter_by(user_id=_user_id).first()
    )
    userAdministrator.administrator_id = administrator_id
    session.commit()
    return 1


def getAdministrator(_email):
    administrator = session.query(Administrator).filter_by(email=_email).first()
    return administrator


def insertAdministrator(firstname, lastname, email, is_super, password):
    admin = session.query(Administrator).filter_by(email=email).first()
    if admin:
        return -1
    salt, pw_hash = hash_new_password(password)
    new_admin = Administrator(
        salt=salt,
        hash=pw_hash,
        email=email,
        dob=date.today(),
        first_name=firstname,
        last_name=lastname,
        is_super=is_super,
        is_active=1,
    )
    session.add(new_admin)
    session.commit()
    return new_admin.id
