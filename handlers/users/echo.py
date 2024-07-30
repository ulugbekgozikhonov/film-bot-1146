from loader import dp
from aiogram import types

@dp.message_handler(content_types="text")
async def echo_handler(message:types.Message):
    await message.answer(message.text)