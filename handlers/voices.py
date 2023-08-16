import os

import speech_recognition as sr
from aiogram import types

from handlers.commands import get_interests, get_photos, get_repo, get_voices
from loader import bot, dp
from settings import MEDIA_ROOT, VOICE_COMPRASION

r = sr.Recognizer()

func_comprasion = {
    'interests': get_interests,
    'photos': get_photos,
    'voices': get_voices,
    'repo': get_repo,
}


def recognize(filename):
    with sr.AudioFile(filename) as source:
        audio_text = r.listen(source)
        text = r.recognize_google(audio_text, language='ru_RU')
    return text


def transformate_ogg_to_wav(path_ogg):
    os.system(
        'ffmpeg -i ' + path_ogg + '  ' + (path_wav := (path_ogg[:-4] + '.wav'))
    )
    return path_wav


async def download_voice(message):
    await bot.download_file(
        (await message.voice.get_file()).file_path,
        path := f'{MEDIA_ROOT}/{message.chat.id}.ogg',
    )
    return path


@dp.message_handler(content_types=('voice',))
async def get_voice(message: types.Message):
    path_ogg = await download_voice(message)
    path_wav = transformate_ogg_to_wav(path_ogg)
    text = recognize(path_wav).lower()
    os.remove(path_ogg)
    os.remove(path_wav)
    for key, value in VOICE_COMPRASION.items():
        for word in text.split():
            if word in value:
                await func_comprasion[key](message)
                return
    await message.answer('Ой, я пока не умею этого делать 🙈')
