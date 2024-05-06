import logging
import asyncio
from config.config import settings
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import time

async def main():
    bot = Bot(token=settings.token.get_secret_value())
    dp = Dispatcher()
    # dp.include_router()
    await dp.start_polling(bot, on_startup=on_startup)
        
def times():
    time_local = time.localtime(time.time())
    format_time = time.strftime("%m-%d | %H:%M", time_local)
    return format_time

async def on_startup(_):
    await bot.send_message('7114989320', f"Bot started in {times()}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        print(f"Бот запущен в {times()}")
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"Бот выключен в {times()}")
