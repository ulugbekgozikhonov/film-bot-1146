from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .user_in_channel import IsUserInChannel


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(IsUserInChannel())
