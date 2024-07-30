from data.config import CHANNELS
from aiogram import types
from loader import bot

async def chek_user_in_channel(message: types.Message):
    user_not_in_channel = []
    for channel_id,channel_url in CHANNELS.items():
        user_id = message.chat.id
        
        member = await bot.get_chat_member(chat_id=channel_id,user_id=user_id)
        if member.status in ("member","owner","creator","administrator"):
            continue
        else:
           user_not_in_channel.append(channel_url)
           
    return user_not_in_channel