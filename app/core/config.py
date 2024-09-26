from pydantic_settings import BaseSettings
from dotenv import load_dotenv

from constants import APP_TITLE, ENV_FILE_NAME

load_dotenv()


class Settings(BaseSettings):
    """Считывать переменные окружения из файла."""
    app_title: str = APP_TITLE
    database_url: str

    class Config:
        """Файл с переменными окружения."""
        env_file = ENV_FILE_NAME


settings = Settings()
