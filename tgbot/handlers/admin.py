from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.handlers.help import get_help_message


async def admin_start(message: Message):
    start_message = f"Здравствуйте, {message.from_user.first_name}!\n"
    start_message += get_help_message()
    await message.reply(start_message)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
