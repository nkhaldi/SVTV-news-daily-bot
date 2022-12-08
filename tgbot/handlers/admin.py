from aiogram import Dispatcher
from aiogram.types import Message


async def admin_start(message: Message):
    msg = f"Hello, master {message.from_user.first_name}"
    await message.reply(msg)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
