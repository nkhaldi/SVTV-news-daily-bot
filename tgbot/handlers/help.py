from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message


def get_help_message():
    help_message = "Раз в день я буду пересылать тебе посты из @svtvnews, "
    help_message += "резюмирующие события, произошедшие за день.\n"
    return help_message


async def cmd_help(message: Message):
    help_message = get_help_message()
    await message.reply(help_message)


async def call_help(callback: CallbackQuery):
    help_message = get_help_message()
    await callback.message.reply(help_message)


def register_help(dp: Dispatcher):
    dp.register_message_handler(cmd_help, commands=["help"], state="*")
