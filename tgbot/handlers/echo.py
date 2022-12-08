from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode


async def bot_echo(message: types.Message):
    echo = f"Эхо без состояния: {message.text}"
    await message.answer(echo)


async def bot_echo_state(message: types.Message, state: FSMContext):
    state_name = await state.get_state()
    echo = f"Эхо в состоянии {hcode(state_name)}: {hcode(message.text)}"
    await message.answer(echo)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo)
    dp.register_message_handler(bot_echo_state, content_types=types.ContentTypes.ANY, state="*")
