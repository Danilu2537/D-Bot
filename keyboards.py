from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

from settings import COMMANDS, PHOTO_CALLBACK, VOICE_CALLBACK

MAIN_BUTTONS = [KeyboardButton(text=text) for text in COMMANDS.values()]
PHOTO_BUTTONS = [
    InlineKeyboardButton(text=text, callback_data=callback)
    for callback, text in PHOTO_CALLBACK.items()
]
VOICE_BUTTONS = [
    InlineKeyboardButton(text=text, callback_data=callback)
    for callback, text in VOICE_CALLBACK.items()
]
main_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True, row_width=1
)
voice_keyboard = InlineKeyboardMarkup(row_width=1)
photo_keyboard = InlineKeyboardMarkup()

main_keyboard.add(*MAIN_BUTTONS)
voice_keyboard.add(*VOICE_BUTTONS)
photo_keyboard.add(*PHOTO_BUTTONS)
