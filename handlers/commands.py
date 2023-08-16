from aiogram import types

from keyboards import main_keyboard
from loader import dp
from settings import COMMANDS, REPO_URL


@dp.message_handler(commands=('start',))
async def get_start_info(message: types.Message):
    await message.answer(
        text='Привет 🙃\n'
        'Я Данила. Давай познакомимся! Выбери, '
        'что бы ты хотел узнать?',
        reply_markup=main_keyboard,
    )


@dp.message_handler(commands=('interests',))
@dp.message_handler(text=COMMANDS['interests'])
async def get_interests(message: types.Message):
    pass


@dp.message_handler(commands=('repo',))
@dp.message_handler(text=COMMANDS['repo'])
async def get_repo(message: types.Message):
    await message.answer(
        f'Вот же тот самый [репозиторий]({REPO_URL}) 🤘', parse_mode='Markdown'
    )
