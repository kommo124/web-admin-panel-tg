from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel  # Добавьте импорт
from bot import bot


class MessageRequest(BaseModel):
    chat_id: int
    text: str

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