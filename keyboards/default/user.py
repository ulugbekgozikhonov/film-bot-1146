from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

def share_contact(text):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=text,request_contact=True)
            ]
        ],resize_keyboard=True
    )