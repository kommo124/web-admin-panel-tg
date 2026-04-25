from aiogram import Router, types
from aiogram.filters import Command
from database import addUser, getAllUsers
import logging

router = Router()

@router.message(Command('start'))
async def cmd_start(message: types.Message):
    userid = message.from_user.id
    if addUser(userid):
        await message.answer("Вы успешно зарегестрировались")
        print(f'Пользователь: {userid} был успешно занесён в бд')
    else:
        print("Что-то пошло не так")


