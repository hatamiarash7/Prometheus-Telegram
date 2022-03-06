import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api_v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    X_API_TOKEN: str = 'no-secret-yet'
    PROJECT_NAME: str = 'Telegram Bot Sender'
    PROJECT_DESCRIPTION: str = 'Telegram handler for Prometheus Alertmanager'
    PROJECT_VERSION: str = '1.0.0'
    TG_BOT_TOKEN: str = '291043804:AAGHDLwaXNN2U2oI0uxCR35KsivsxNUqT3o'
    TG_API_ID: str = '45491'
    TG_API_HASH: str = '12e2adfabe4fb77970b6bae2823taf92'
    TG_SESSION_NAME: str = 'tg_session_sender'

    TG_FILES_CHAT_ID: int = 0

    class Config:
        case_sensitive = True


settings = Settings()
