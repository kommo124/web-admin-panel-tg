import asyncio
import logging
from aiogram import Bot, Dispatcher
from database import init_db, getAllUsers
from handlers.start import router
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')

if not TOKEN:
    raise ValueError("Токен не указан")

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    
    init_db()
    print(getAllUsers())
    
    dp.include_router(router)
    logging.info("Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nБот остановлен")