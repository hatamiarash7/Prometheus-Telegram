from pydantic import BaseModel


class PlainMessageSend(BaseModel):
    chat_id: int
    text: str


class Alert(BaseModel):
    type: str
    summary: str
    alert_name: str
    instance: str
    serverity: str
    status: str
