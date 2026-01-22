from pydantic import BaseModel
from datetime import datetime

# общие поля
class ChatBase(BaseModel):
    title: str

# для POST создать чат
class ChatCreate(ChatBase):
    pass

# для GET
class ChatResponse(ChatBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True