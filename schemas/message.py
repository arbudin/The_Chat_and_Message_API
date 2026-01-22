from pydantic import BaseModel, constr
from datetime import datetime

class MessageBase(BaseModel):
    # валидация на лишние пробелы и ограничения длины текста
    text: constr(strip_whitespace=True, min_length=1, max_length=5000)

# для POST
class MessageCreate(MessageBase):
    pass

# для GET
class MessageResponse(MessageBase):
    id: int
    chat_id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }