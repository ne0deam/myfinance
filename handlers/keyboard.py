from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(
            KeyboardButton(text="Ввод данных доход/расход"),
            KeyboardButton(text="Создание названий статей доход/расход"),
            KeyboardButton(text="Баланс")
    ), builder.adjust(1, 1, 1)

    return builder.as_markup(resize_keyboard=True)

menu_keyboard = menu_keyboard()

