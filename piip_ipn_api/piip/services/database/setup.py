from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from piip.constants import DATABASE, HOST, PASSWORD, USERNAME

database_route = f"mysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"

engine = create_engine(
    database_route,
    encoding="utf8",
    pool_pre_ping=True,
    connect_args={"connect_timeout": 25},
    pool_size=20,
    pool_recycle=300,
)
Session = sessionmaker(bind=engine)
session = scoped_session(Session)
