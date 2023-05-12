import os


class Config:
    APP_ENV = os.getenv("APP_ENV", "development")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")

    # URLs for the services this gateway communicates with
    SERVICE_URLS = {
        "auth": os.getenv("AUTH_SERVICE_URL", "http://auth:8000"),
        "core": os.getenv("CORE_SERVICE_URL", "http://core:8001"),
    }
