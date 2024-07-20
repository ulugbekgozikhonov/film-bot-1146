from aiogram import types
from aiogram.dispatcher import FSMContext
from states.user import RegisterState
from loader import dp,dbmanager
from keyboards.default.user import share_contact
from utils.db_api.query import insert_user


@dp.callback_query_handler(state=RegisterState.langugae)
async def language_handler(call:types.CallbackQuery,state:FSMContext):
    lang = call.data
    await state.update_data(lang=lang)
    if lang == "uz":
        await call.message.answer("Ism familyaingizni kiriting:")
    elif lang == "ru":
        await call.message.answer("Введите свое имя:")
    else:
        await call.message.answer("Enter full name:")
    
    await call.answer()
    await RegisterState.ful_name.set()
    
@dp.message_handler(state=RegisterState.ful_name)
async def full_name_handler(message:types.Message,state:FSMContext):
    full_name = message.text
    await state.update_data(full_name=full_name)
    data = await state.get_data()
    lang = data.get("lang")
    if lang == "uz":
        await message.answer("Telefon raqamingiz yuboring:",reply_markup=share_contact(text="Telefonni ulashish"))
    elif lang == "ru":
        await message.answer("Поделиться контактом:",reply_markup=share_contact(text="Поделиться контактом"))
    else:
        await message.answer("Share Contact:",reply_markup=share_contact(text="Share contact"))
    
    await RegisterState.phone_number.set()
    
@dp.message_handler(state=RegisterState.phone_number,content_types="contact")
async def full_name_handler(message:types.Message,state:FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    data = await state.get_data()
    lang = data.get("lang")
    if lang == "uz":
        await message.answer("Botdan Foydalanish uchun Kanallarga azo bo'lishing kerak🤬🤬")
    elif lang == "ru":
        await message.answer("Вы должны подписаться на каналы, чтобы использовать бота")
    else:
        await message.answer("You need to subscribe to the channels to use the bot:")
    
    data = await state.get_data()
    data_tuple = (data['full_name'],data['phone_number'],data['chat_id'],data['lang'])
    dbmanager.insert_data(insert_sql=insert_user,data=data_tuple)
    await state.finish()