from app import schemas
from app.config import settings

TG_CHAT_ID = settings.TG_CHAT_ID
FIRE_EMOJI = "\U0001f631"
RESOLVED_EMOJI = "\U00002705"


def format_alert(fired, severity, date, summary, description):
    emoji = FIRE_EMOJI if fired else RESOLVED_EMOJI
    action = "New alert received" if fired else "Problem resolved"

    return schemas.PlainMessageSend(
        chat_id=TG_CHAT_ID,
        text=f"{emoji} {action} {emoji}\n\n*severity*: {severity}\n\n*date*: {date}\n\n*summary*: {summary}\n\n*description*: {description}"
    )
