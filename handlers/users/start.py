from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.inline.user import language
from states.user import RegisterState


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message,state:FSMContext):
    await message.answer("Choose Language",reply_markup=language)
    chat_id = message.chat.id
    await state.update_data(chat_id=chat_id)
    await RegisterState.langugae.set()
