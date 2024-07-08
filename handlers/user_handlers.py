
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from keyboards.keyboards import get_buttons
from lexicon.lexicon_ru import LEXICON_RU

router = Router()


# Обработчик команды /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        LEXICON_RU['/start'],
        reply_markup=get_buttons().as_markup(resize_keyboard=True)
    )


# Обработчик команды /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
