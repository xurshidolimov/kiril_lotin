from aiogram import types
from transliterate import to_cyrillic, to_latin
from loader import dp



@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    if message.text.isascii():
        await message.answer(to_cyrillic(message.text))
    else:
        await message.answer(to_latin(message.text))