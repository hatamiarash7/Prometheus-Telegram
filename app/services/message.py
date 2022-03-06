from typing import Optional, NoReturn

from app import schemas
from app.config import bot_init


async def send_message(message: schemas.PlainMessageSend) -> Optional[NoReturn]:
    async with await bot_init() as bot:
        await bot.send_message(message.chat_id, message.text)
