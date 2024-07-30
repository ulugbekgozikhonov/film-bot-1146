
from loader import dp
from .users import IsPrivateChat
if __name__ == "filters":
    dp.filters_factory.bind(IsPrivateChat)
