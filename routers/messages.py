from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import Message, Chat
from schemas import chat
from schemas.message import MessageResponse, MessageCreate

router = APIRouter()

@router.get("/", response_model=List[MessageResponse])
def get_messages(db: Session = Depends(get_db)):
    return db.query(Message).all()

@router.post("/", response_model=MessageResponse)
def post_message(message: MessageCreate, db: Session = Depends(get_db)):

    # проверка на существующий чат
    chat = db.query(Chat).filter(Chat.id == message.chat_id).first()
    if not chat:
        raise HTTPException(
            status_code=404,
            detail="Нельзя отправит сообщение в несуществующий чат"
        )

    new_message = Message(
        text=message.text,
        chat_id=message.chat_id,
    )
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message

#удалить сообщение
@router.delete("/{message_id}", status_code=204)
def delete_message(message_id: int, db: Session = Depends(get_db)):
    message = db.query(Message).filter(Message.id == message_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Сообщение не найдено")

    db.delete(message)
    db.commit()
    return