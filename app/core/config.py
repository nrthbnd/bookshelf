import os
from dotenv import load_dotenv
from typing import Optional
from pydantic import EmailStr
from pydantic_settings import BaseSettings

from constants import APP_TITLE, ENV_FILE_NAME

load_dotenv()


class Settings(BaseSettings):
    """Считывать переменные окружения из файла."""
    app_title: str = APP_TITLE
    database_url: str
    secret: str = os.getenv('SECRET')
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    class Config:
        """Файл с переменными окружения."""
        env_file = ENV_FILE_NAME


settings = Settings()
