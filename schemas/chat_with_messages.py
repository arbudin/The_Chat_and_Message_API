from datetime import datetime
from typing import List
from pydantic import BaseModel
from schemas.message import MessageResponse


class ChatWithMessages(BaseModel):
    id: int
    title: str
    created_at: datetime
    messages: List[MessageResponse]

    model_config = {
        "from_attributes": True
    }