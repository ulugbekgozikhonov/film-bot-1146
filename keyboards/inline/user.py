from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from loader import dbmanager
from utils.db_api.query import get_channles
language = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 Uzbek",callback_data="uz"),
            InlineKeyboardButton(text="🇷🇺 Русский",callback_data="ru"),
        ],
        [
            InlineKeyboardButton(text="🇺🇸 English",callback_data="en"),
        ]
    ]
)

def channels(lang):
    channels = dbmanager.query_data_fetch_all(get_channles)
    channels_markup = InlineKeyboardMarkup()
    
    if channels:
        for i,channel in enumerate(channels):
            if lang == "uz":
                button = InlineKeyboardButton(text=f"{i+1}-kanal",callback_data=f"channel_{i+1}",url=channel[1])
            elif lang == "ru":
                button = InlineKeyboardButton(text=f"{i+1}-канал",callback_data=f"channel_{i+1}",url=channel[1])
            elif lang == "en":
                button = InlineKeyboardButton(text=f"{i+1}-channel",callback_data=f"channel_{i+1}",url=channel[1])
            channels_markup.add(button)
            
        return channels_markup
        

#     InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Men dasturchiman",callback_data="channel_1",url="https://t.me/mendasturchiman")
#         ],
#         [
#             InlineKeyboardButton(text="Tasdiql")
#         ]
#     ]
# )