from typing import Optional, NoReturn
from urllib.parse import quote

import requests

from app import schemas, config


async def send_message(message: schemas.PlainMessageSend) -> Optional[NoReturn]:
    tg_url = f"{config.settings.TG_HOST}/bot{config.settings.TG_BOT_TOKEN}/sendMessage?parse_mode=MarkdownV2"

    data = {
        "chat_id": message.chat_id,
        "text": fix_body(message.text)
    }
    response = requests.post(tg_url, data)
    response.raise_for_status()
    return response.content.decode()


def fix_body(body: str) -> str:
    return body.replace("_", '\\_').replace("[", '\\[').replace("]", '\\]').replace("(", '\\(').replace(")", '\\)').replace("~", '\\~').replace("`", '\\`').replace(">", '\\>').replace("#", '\\#').replace("+", '\\+').replace("-", '\\-').replace("=", '\\=').replace("|", '\\|').replace("{", '\\{').replace("}", '\\}').replace(".", '\\.').replace("!", '\\!')
