from piip.models import Problem
from piip.services.database.setup import session


def get_problem_by_url(url):
    return session.query(Problem).filter(url=url).first()
