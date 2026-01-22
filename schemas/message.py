from pydantic import BaseModel
from datetime import datetime

class MessageBase(BaseModel):
    text: str
    chat_id: int

# для POST
class MessageCreate(MessageBase):
    pass

# для GET
class MessageResponse(MessageBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True