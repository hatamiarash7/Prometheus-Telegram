import os
from app import schemas


def formatFiredAlert(severity, date, summary, description):
    emoji = "\U0001f631"

    return schemas.PlainMessageSend(
        chat_id=os.environ['TG_CHAT_ID'],
        text="{} New alert received {}\n\n**severity** = {}\n**date** = {}\n**summary** = {}\n**description** = {}".format(
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
        chat_id=os.environ['TG_CHAT_ID'],
        text="{} Problem resolved {}\n\n**severity** = {}\n**date** = {}\n**summary** = {}\n**description** = {}".format(
            emoji,
            emoji,
            severity,
            date,
            summary,
            description
        )
    )
