from sqlmodel import create_engine, Session
from . import Config

SQLALCHEMY_DATABASE_URL = f"postgresql://{Config.POSTGRES_USER}:{Config.POSTGRES_PASSWORD}@{Config.DATABASE_HOST}/{Config.DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
