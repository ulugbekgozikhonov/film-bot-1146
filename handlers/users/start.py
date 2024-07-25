from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp,dbmanager
from keyboards.inline.user import language,channels
from states.user import RegisterState
from utils.db_api.query import get_user_by_chat_id

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message,state:FSMContext):
    chat_id = message.chat.id
    user = dbmanager.query_data_fetch_one(get_user_by_chat_id,(chat_id,))
    print(user)
    lang = user[-1]
    if user:
        if lang == "uz":
            await message.answer("Kanalarga a'zo bo'ling",reply_markup=channels(lang))
        elif lang == "en":
            await message.answer("You have to subscribe channels",reply_markup=channels(lang))
        elif lang == "ru":
            await message.answer("Вам необходимо подписаться на каналы",reply_markup=channels(lang))
    else:
        await message.answer("Choose Language",reply_markup=language)
        await state.update_data(chat_id=chat_id)
        await RegisterState.langugae.set()

