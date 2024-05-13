import logging
import asyncio
from config.config import settings
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import time
from handlers.handler import router


async def main():
    bot = Bot(token=settings.token.get_secret_value())
    dp = Dispatcher()
    dp.include_router(router=router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
        
def times():
    time_local = time.localtime(time.time())
    format_time = time.strftime("%m-%d | %H:%M", time_local)
    return format_time

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        print(f"Бот запущен в {times()}")
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"Бот выключен в {times()}")
