import datetime

import gspread
from aiogram import F, Router
from aiogram.types import Message
from oauth2client.service_account import ServiceAccountCredentials

from lexicon.lexicon_ru import LEXICON_RU
from services.get_image import get_new_image

router = Router()

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("bot1.json", scope)
client = gspread.authorize(creds)
SHEET = client.open("Bot").sheet1


# Обработчик первой кнопки
@router.message(F.text == "Кнопка 1")
async def handle_button1(message: Message):
    await message.answer(LEXICON_RU['Кнопка 1'])


# Обработчик второй кнопки
@router.message(F.text == "Кнопка 2")
async def handle_button2(message: Message):
    await message.answer(LEXICON_RU['Кнопка 2'])


# Обработчик третьей кнопки
@router.message(F.text == "Кнопка 3")
async def handle_button3(message: Message):
    await message.answer_photo(get_new_image(), caption=LEXICON_RU['Кнопка 3'])


# Обработчик четвёртой кнопки
@router.message(F.text == "Кнопка 4")
async def handle_button4(message: Message):
    value_A2 = SHEET.acell('A2').value
    await message.answer(f"Значение A2 в таблице: {value_A2}")


# Обработчик проверки даты
@router.message()
async def check_date(message: Message):
    input_date = message.text
    # проверяю формат даты на соответствие дд.мм.гг
    try:
        date_format = "%d.%m.%y"
        datetime.datetime.strptime(input_date, date_format)
        # если дата верна, заносим её в следующий ряд столбца В
        SHEET.append_row([input_date], value_input_option='USER_ENTERED')
        await message.answer("Дата введена верно.")
    except ValueError:
        await message.answer("Дата введена неверно.")
