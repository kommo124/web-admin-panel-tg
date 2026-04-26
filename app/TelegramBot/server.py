from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
from aiogram import Bot
from database import getAllUsers, getAllUsersAsNumber

# ===== Модели =====
class MessageRequest(BaseModel):
    chat_id: int
    text: str
    token: str

class SendAllRequest(BaseModel):
    text: str
    delay_between_messages: float = 0.5
    token: str

# ===== Инициализация =====
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ===== Роуты =====
@app.get("/")
async def root():
    return {"message": "Server is running"}

# ===== Отправка одному =====
@app.post("/send")
async def send_message(request: MessageRequest):
    try:
        async with Bot(token=request.token) as bot:
            await bot.send_message(
                chat_id=request.chat_id,
                text=request.text
            )
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ===== Отправка всем =====
@app.post("/sendAll")
async def send_all(request: SendAllRequest):
    users = getAllUsers()

    if not users:
        return {"status": "no users"}

    try:
        async with Bot(token=request.token) as bot:
            for user_id in users:
                try:
                    await bot.send_message(
                        chat_id=user_id,
                        text=request.text
                    )
                    await asyncio.sleep(request.delay_between_messages)
                except Exception as user_error:
                    print(f"Ошибка для {user_id}: {user_error}")

        return {"status": "ok"}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

# ===== Статистика =====
@app.get("/stats")
async def stats():
    total = getAllUsersAsNumber()
    return {"total_users": total[0]}