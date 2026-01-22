from typing import Union

from fastapi import FastAPI

from routers import chats, messages

app = FastAPI()

app.include_router(chats.router, prefix="/chats", tags=["Chats"])
app.include_router(messages.router, prefix="/messages", tags=["Messages"])

