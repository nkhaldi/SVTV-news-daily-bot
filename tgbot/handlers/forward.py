from aiogram import types, Dispatcher
# from aiogram.dispatcher import FSMContext
# from aiogram.utils.markdown import hcode


async def bot_forward(message: types.Message):
    await message.forward(message.chat.id, message.message_thread_id)


def register_forward(dp: Dispatcher):
    dp.register_message_handler(bot_forward, content_types=types.ContentTypes.ANY)
