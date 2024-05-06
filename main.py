import logging
import asyncio
from config.config import settings
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.token.get_secret_value())

dp=Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message()
async def mirror_msg(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
