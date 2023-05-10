import os


class Config:
    APP_ENV = os.getenv("APP_ENV", "development")
    DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "user")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "password")
    DATABASE_HOST = os.getenv("DATABASE_HOST", "db")
    DATABASE_NAME = os.getenv("DATABASE_NAME_AUTH", "auth_db")
    JWT_SECRET = os.getenv("JWT_SECRET", "your-secret-key")
