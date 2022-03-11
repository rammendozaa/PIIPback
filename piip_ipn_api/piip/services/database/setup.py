from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


USERNAME = "admin"
PASSWORD = "*&WcgpYU4-.{mt.-"
HOST = "127.0.0.1"
DATABASE = "PIIP_pruebas"


database_route = f"mysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"

engine = create_engine(
    database_route,
    encoding="utf8",
    pool_pre_ping=True,
    connect_args={"connect_timeout": 25},
    pool_size=20,
    pool_recycle=300
)
Session = sessionmaker(bind=engine)
session = scoped_session(Session)
