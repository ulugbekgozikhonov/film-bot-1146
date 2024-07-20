from aiogram.dispatcher.filters.state import StatesGroup,State

class RegisterState(StatesGroup):
    langugae = State()
    ful_name = State()
    phone_number = State()