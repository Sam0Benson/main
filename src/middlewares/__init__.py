from aiogram import Dispatcher

from src.middlewares.exists_user import ExistsUserMiddleware
from src.middlewares.throttling import ThrottlingMiddleware


# Подключение милдварей
def setup_middlewares(dp: Dispatcher):
    dp.middleware.setup(ExistsUserMiddleware())
    dp.middleware.setup(ThrottlingMiddleware())