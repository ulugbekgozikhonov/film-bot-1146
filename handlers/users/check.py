from loader import dp,dbmanager
from aiogram import types
from utils.misc.check_user import chek_user_in_channel
from utils.db_api.query import get_user_by_chat_id


@dp.callback_query_handler(text="confirm")
async def confirm_handler(call:types.CallbackQuery):
    user_not_in_channel = await chek_user_in_channel(message=call.message)
    user = dbmanager.query_data_fetch_one(get_user_by_chat_id,(call.message.chat.id,))
    lang = user[-1]
    if user_not_in_channel:
        await call.answer("Hamma kanalarga a'zo bo'ling",show_alert=True)
    else:
        if lang == "uz":
            await call.message.answer("Film kodini yuboring:")
        elif lang == "en":
            await call.message.answer("Send film code:")
        elif lang == "ru":
            await call.message.answer("Отправить код фильма:")
    
    await call.answer()
    