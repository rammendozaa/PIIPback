from piip.services.database.setup import session
from datetime import date
from piip.models import DictSchool, User


def prueba():
    school = session.query(DictSchool).get(1)
    print(f"School name: {school.name}")
    some_user = User(email="email", password="unsafe", dob=date.today(), first_name="Prueba", last_name="Prueba Apellido", school_id=1)
    session.add(some_user)
    session.commit()
    print(f"User name: {some_user.first_name}")
    print(f"User school: {some_user.school_id}")
    print(f"User school: {some_user.school.id}")
    print(f"User school: {some_user.school.name}")
    print(f"User school: {some_user.school.description}")
    return some_user