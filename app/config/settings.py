import secrets
import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api_v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    X_API_TOKEN: str = 'no-secret-yet'
    PROJECT_NAME: str = 'Telegram Bot Sender'
    PROJECT_DESCRIPTION: str = 'Telegram handler for Prometheus Alertmanager'
    PROJECT_VERSION: str = '1.0.0'
    TG_BOT_TOKEN: str = os.environ['TG_BOT_TOKEN']
    TG_API_ID: str = os.environ['TG_API_ID']
    TG_API_HASH: str = os.environ['TG_API_HASH']
    TG_SESSION_NAME: str = 'tg_session_sender'

    TG_FILES_CHAT_ID: int = 0

    class Config:
        case_sensitive = True


settings = Settings()
