from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from handlers import keyboard

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(text="Выберите действие", reply_markup=keyboard.menu_keyboard)

@router.message(F.text == "Ввод данных доход/расход")
async def write_data(message: Message):
    await message.answer(text="Выберите действие")

