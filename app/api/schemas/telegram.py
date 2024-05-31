import pydantic


class MessageData(pydantic.BaseModel):
    message_text: str
    from_phone: str
    username: str
