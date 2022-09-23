from app import schemas
from app.config import settings


def formatFiredAlert(severity, date, summary, description):
    emoji = "\U0001f631"

    return schemas.PlainMessageSend(
        chat_id=settings.TG_CHAT_ID,
        text="{} New alert received {}\n\n*severity*: {}\n\n*date*: {}\n\n*summary*: {}\n\n*description*: {}".format(
            emoji,
            emoji,
            severity,
            date,
            summary,
            description
        )
    )


def formatResolvedAlert(severity, date, summary, description):
    emoji = "\U00002705"

    return schemas.PlainMessageSend(
        chat_id=settings.TG_CHAT_ID,
        text="{} Problem resolved {}\n\n*severity*: {}\n\n*date*: {}\n\n*summary*: {}\n\n*description*: {}".format(
            emoji,
            emoji,
            severity,
            date,
            summary,
            description
        )
    )
