from typing import List

from fastapi import APIRouter, HTTPException, Query
from fastapi.params import Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import Chat, Message
from schemas.chat import ChatCreate, ChatResponse
from schemas.chat_with_messages import ChatWithMessages
from schemas.message import MessageResponse, MessageCreate

router = APIRouter()

# получить N сообщений из чата
@router.get("/{chat_id}", response_model=ChatWithMessages)
def get_chat_with_messages(
    chat_id: int,
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        raise HTTPException(status_code=404, detail="Чат не найден")

    messages = (
        db.query(Message)
        .filter(Message.chat_id == chat.id)
        .order_by(Message.created_at.desc())
        .limit(limit)
        .all()
    )

    messages_response = [MessageResponse.from_orm(m) for m in messages]

    return ChatWithMessages(
        id=chat.id,
        title=chat.title,
        created_at=chat.created_at,
        messages=messages_response
    )

# добавить сообщение по указанному chat_id
@router.post("/{chat_id}/messages/", response_model=MessageResponse)
def post_message_to_chat(chat_id: int, message: MessageCreate, db: Session = Depends(get_db)):

    # проверка на существующий чат
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        raise HTTPException(
            status_code=404,
            detail="Нельзя отправит сообщение в несуществующий чат"
        )

    new_message = Message(
        text=message.text,
        chat_id=chat_id,
    )
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message

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