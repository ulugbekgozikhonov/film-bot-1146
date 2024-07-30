from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import Update
from loader import dp
from utils.misc.check_user import chek_user_in_channel
from keyboards.inline.user import channels
class IsUserInChannel(BaseMiddleware):
    
    async def on_pre_process_update(self, update: Update, data: dict):
        
        if update.callback_query:
            if update.callback_query.data in("confirm","uz","ru","en"):
                return
            else:
                message = update.callback_query.message
    
        elif update.message:
            text = update.message.text
            if text in ("/start","/help"):
                return
            else:
                message = update.message
        
        state = dp.current_state(chat=message.chat.id,user=message.from_user.id)
        if state:
            current_state = await state.get_state()
            if current_state:
                current_state = current_state.split(":")
                if current_state[0] == "RegisterState":
                    return
          
        user_not_in_channel = await chek_user_in_channel(message=message)
        if user_not_in_channel:
            await message.answer("Kanalarga a'zo bo'lmagansiz",reply_markup=channels("uz",channels=user_not_in_channel))
            raise CancelHandler()
        return