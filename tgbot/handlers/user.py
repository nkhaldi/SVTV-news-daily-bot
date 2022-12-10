from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.handlers.help import get_help_message


async def user_start(message: Message):
    start_message = f"Привет, {message.from_user.first_name}!\n"
    start_message += get_help_message()
    await message.reply(start_message)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
