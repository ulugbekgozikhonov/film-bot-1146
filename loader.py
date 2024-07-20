from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.database import DatabaseManager

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dbmanager = DatabaseManager(config.DB_NAME,config.DB_USER,config.DB_PASSWORD,config.DB_HOST,config.DB_PORT)