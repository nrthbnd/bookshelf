import os
from dotenv import load_dotenv
from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from constants import APP_TITLE, ENV_FILE_NAME

load_dotenv()


class Settings(BaseSettings):
    """Считывать переменные окружения из файла."""
    app_title: str = APP_TITLE
    database_url: str
    secret: str = os.getenv('SECRET')
    first_superuser_email: EmailStr | None = None
    first_superuser_password: str | None = None
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    model_config = SettingsConfigDict(
        env_file=ENV_FILE_NAME,
        extra="ignore",
    )


settings = Settings()
