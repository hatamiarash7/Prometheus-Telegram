import string
from typing import Optional, NoReturn

from app import schemas, config
import requests


async def send_message(message: schemas.PlainMessageSend) -> Optional[NoReturn]:
    TG_URL = "%s/bot%s/sendMessage?parse_mode=MarkdownV2" % (
        config.settings.TG_HOST, config.settings.TG_BOT_TOKEN)

    data = {
        "chat_id": message.chat_id,
        "text": fixBody(message.text)
    }
    print(requests.post(TG_URL, data).content)


def fixBody(body: string) -> string:
    return body.replace("[", "\\[").replace("`", "\\`").replace("=", "\\=").replace("-", "\\-")
