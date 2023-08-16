from aiogram import types

from keyboards import main_keyboard
from loader import dp


@dp.message_handler(commands=('start',))
async def get_start_info(message: types.Message):
    await message.answer(
        text='Привет!\n'
        'Я Данила! Давай мы с тобой познакомимся, выбери, '
        'что бы ты хотел узнать',
        reply_markup=main_keyboard,
    )
