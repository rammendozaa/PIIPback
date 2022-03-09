from sqlalchemy import null
from piip.services.database.setup import session
from piip.models import Administrator, UserAdministrator

def assignStudent(_email,_user_id):
    administrator = session.query(Administrator).filter_by(email=_email).first()
    administrator_id = administrator.id

    userAdministrator = session.query(UserAdministrator).filter_by(user_id=_user_id).first();
    userAdministrator.administrator_id = administrator_id
    session.commit()
    return 1
    
def getAdministrator(_email):
    administrator = session.query(Administrator).filter_by(email=_email).first()
    return administrator