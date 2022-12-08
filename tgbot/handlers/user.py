from aiogram import Dispatcher
from aiogram.types import Message


async def user_start(message: Message):
    msg = f"Hello, {message.from_user.first_name}"
    await message.reply(msg)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
