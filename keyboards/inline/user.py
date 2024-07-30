from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
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

def channels(lang,channels):
    channels_markup = InlineKeyboardMarkup()
    
    if channels:
        text = ""
        for i,url in enumerate(channels):
            if lang == "uz":
                button = InlineKeyboardButton(text=f"{i+1}-kanal",callback_data=f"channel_{i+1}",url=url)
                text="✅Tasdiqlash"
            elif lang == "ru":
                button = InlineKeyboardButton(text=f"{i+1}-канал",callback_data=f"channel_{i+1}",url=url)
                text="✅Подтверждение"
            elif lang == "en":
                button = InlineKeyboardButton(text=f"{i+1}-channel",callback_data=f"channel_{i+1}",url=url)
                text = "✅Confirmation"
            channels_markup.add(button)
            
        return channels_markup.add(InlineKeyboardButton(text=text,callback_data="confirm"))
        

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