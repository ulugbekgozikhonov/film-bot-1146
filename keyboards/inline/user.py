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