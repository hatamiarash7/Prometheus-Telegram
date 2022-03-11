from pydantic import BaseModel


class PlainMessageSend(BaseModel):
    chat_id: int
    text: str
