from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp,dbmanager
from states.user import RegisterState
from utils.db_api.query import get_user_by_chat_id
from filters.users import IsPrivateChat
from keyboards.inline.user import language,channels
from utils.misc.check_user import chek_user_in_channel

@dp.message_handler(IsPrivateChat(),CommandStart())
async def bot_start(message: types.Message,state:FSMContext):
    chat_id = message.from_user.id
    user = dbmanager.query_data_fetch_one(get_user_by_chat_id,(chat_id,))
    if user: 
        lang = user[-1]
        user_not_in_channel = await chek_user_in_channel(message)
        if user_not_in_channel:
            await message.answer("Hamma kanalarga a'zo bo'ling",reply_markup=channels(lang,user_not_in_channel))
        else:
            if lang == "uz":
                await message.answer("Film kodini yuboring:")
            elif lang == "en":
                await message.answer("Send film code:")
            elif lang == "ru":
                await message.answer("Отправить код фильма:")
    else:
        await message.answer("Choose Language",reply_markup=language)
        await state.update_data(chat_id=chat_id)
        await RegisterState.langugae.set()
