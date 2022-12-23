from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from config import Config
from src.data.config import get_admins
from src.data.config import BOT_TOKEN
from src.data.loader import bot

import asyncio

# bot = Bot(token=Config.token)
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot, storage=MemoryStorage())


async def main():
    from handlers import dp
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')


