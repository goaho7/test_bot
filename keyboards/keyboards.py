from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Создание четырёх кнопок
def get_buttons():
    kb_builder = ReplyKeyboardBuilder()
    buttons: list[KeyboardButton] = [
        KeyboardButton(text=f'Кнопка {i + 1}') for i in range(4)
    ]
    kb_builder.row(*buttons, width=2)
    return kb_builder
