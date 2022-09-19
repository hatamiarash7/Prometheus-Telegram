import secrets
import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PREFIX: str = '/api'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    X_API_TOKEN: str = 'no-secret-yet'
    PROJECT_NAME: str = 'Telegram Bot Sender'
    PROJECT_DESCRIPTION: str = 'Telegram handler for Prometheus Alertmanager'
    PROJECT_VERSION: str = '1.1.0'
    TG_HOST: str = os.environ['TG_HOST']
    TG_BOT_TOKEN: str = os.environ['TG_BOT_TOKEN']
    TG_SESSION_NAME: str = 'tg_session_sender'
    TG_CHAT_ID: str = os.environ['TG_CHAT_ID']

    class Config:
        case_sensitive = True


settings = Settings()
