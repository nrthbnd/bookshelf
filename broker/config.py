from os import path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(dotenv_path=path.join(path.dirname(__file__), '..', '.env.rmq'))


class Settings(BaseSettings):
    RMQ_HOST: str
    RMQ_PORT: str
    RMQ_USER: str
    RMQ_PASSWORD: str
    RMQ_QUEUE_NAME: str
    RMQ_CONNECTION_URL: str

    model_config = SettingsConfigDict(env_file=".env.rmq")


settings = Settings()
