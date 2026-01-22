from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import Chat, Message
from schemas.chat import ChatCreate, ChatResponse
from schemas.message import MessageResponse

router = APIRouter()

# получить все чаты
@router.get("/", response_model=List[ChatResponse])
def get_chats(db: Session = Depends(get_db)):
    return db.query(Chat).all()

# получить сообщения по id чата
@router.get("/{chat_id}/messages", response_model=List[MessageResponse])
def get_chat_messages(chat_id: int, db: Session = Depends(get_db)):
    chat = db.query(Chat).filter(Chat.id == chat_id).first()

    if not chat:
        raise HTTPException(status_code=404, detail="Чат не найден")

    return db.query(Message).filter(Message.chat_id == chat_id).all()

# добавить чат
@router.post("/", response_model=ChatResponse)
def create_chat(chat: ChatCreate, db: Session = Depends(get_db)):
    new_chat = Chat(title=chat.title)
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return new_chat

# удалить чат каскадно
@router.delete("/{chat_id}", status_code=204)
def delete_chat(chat_id: int, db: Session = Depends(get_db)):

    # проверяем существует ли чат
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        raise HTTPException(status_code=404, detail="Чат не найден")

    db.delete(chat)
    db.commit()
    return