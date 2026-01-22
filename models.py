from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Chat(Base):
    __tablename__ = 'chats'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)



class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey('chats.id', ondelete='CASCADE'), nullable=False)
    text = Column(String(5000), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
