from piip.models import Template
from piip.services.database.setup import session


def get_template_by_id(id):
    return session.query(Template).get(id)
