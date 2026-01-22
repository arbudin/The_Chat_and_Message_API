from pydantic import BaseModel, constr
from datetime import datetime

# общие поля
class ChatBase(BaseModel):
    # валидация на лишние пробелы и ограничения длины текста
    title: constr(strip_whitespace=True, min_length=1, max_length=200)

# для POST создать чат
class ChatCreate(ChatBase):
    pass

# для GET
class ChatResponse(ChatBase):
    id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }