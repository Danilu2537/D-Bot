from aiogram import types

from keyboards import main_keyboard, photo_keyboard
from loader import dp
from settings import COMMANDS, PHOTO_CALLBACK, PHOTO_PATH, REPO_URL


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


@dp.message_handler(commands=('cancel',))
@dp.message_handler(text=COMMANDS['cancel'])
async def cancel(message: types.Message):
    await message.answer('😢')


@dp.message_handler(commands=('photos',))
@dp.message_handler(text=COMMANDS['photos'])
async def get_photos(message: types.Message):
    await message.answer('Выберите фото 📸', reply_markup=photo_keyboard)


@dp.callback_query_handler(lambda query: query.data in PHOTO_CALLBACK)
async def get_photo(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer_photo(
        types.InputFile(PHOTO_PATH[query.data]), reply_markup=photo_keyboard
    )
