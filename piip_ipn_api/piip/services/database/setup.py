from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


USERNAME = "admin"
PASSWORD = "*&WcgpYU4-.{mt.-"
HOST = "127.0.0.1"
DATABASE = "PIIP_pruebas"


database_route = f"mysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"

engine = create_engine(database_route)
Session = sessionmaker(bind=engine)
session = Session()