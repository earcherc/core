from sqlmodel import create_engine, Session
from .config import Config

SQLALCHEMY_DATABASE_URL = f"postgresql://{Config.DATABASE_USERNAME}:{Config.DATABASE_PASSWORD}@{Config.DATABASE_HOST}/{Config.DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
