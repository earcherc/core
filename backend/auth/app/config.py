import os


class Config:
    APP_ENV = os.getenv("APP_ENV", "development")
    DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE_HOST = os.getenv("DATABASE_HOST", "db")
    DATABASE_NAME = os.getenv("DATABASE_NAME_AUTH")
    JWT_SECRET = os.getenv("JWT_SECRET", "your-secret-key")
