import sqlite3

from aiogram import types

from data.config import ADMINS
from transliterate import to_cyrillic, to_latin
from loader import dp, db, bot


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    if message.text.isascii():
        await message.answer(to_cyrillic(message.text))
    else:
        await message.answer(to_latin(message.text))

    # Foydalanuvchini bazaga qo'shamiz
    name = message.from_user.full_name

    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)
