from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from bot import bot
from database import getAllUsers, getAllUsersAsNumber
import asyncio

class MessageRequest(BaseModel):
    chat_id: int
    text: str

class sendAllRequest(BaseModel):
    text: str
    delay_between_messages: float = 0.5

class allUsersRequest(BaseModel):
    total_users: int

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
async def root():
    return {
        "message": "Telegram Bot API is running",
        "endpoints": {
            "POST /send": "Send message to Telegram",
            "GET /docs": "API documentation"
        }
    }


@app.post('/send')
async def sendMessage(request: MessageRequest):  
    try:
        await bot.send_message(
            chat_id=request.chat_id,  
            text=request.text
        )
        return {"status": "ok", "message": "Message sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/sendAll')
async def sendMessageToAll(request: sendAllRequest):
    users = getAllUsers()
    try:
        for user_id in users:
            await bot.send_message(
                chat_id = user_id,
                text = request.text
            )
            await asyncio.sleep(request.delay_between_messages)
            
        return {"status": "ok", "message": "Message sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stats")
async def usersCount():
    total = getAllUsersAsNumber()
    return{"total_users": total[0]}