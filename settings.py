from pathlib import Path

from envparse import env

BASE_DIR = Path(__file__).resolve().parent

ENV_PATH = BASE_DIR.joinpath('.env')
if ENV_PATH.is_file():
    env.read_envfile(ENV_PATH)

REPO_URL = 'https://github.com/Danilu2537/D-Bot'
BOT_TOKEN = env.str('BOT_TOKEN')

COMMANDS = {
    'photos': 'Мои фотографии 😎',
    'interests': 'Мое главное увлечение 🤓',
    'voices': 'Мои голосовые 🤩',
    'repo': 'Репозиторий этого бота 📚',
    'cancel': 'Отмена 🚫',
}

MEDIA_ROOT = BASE_DIR.joinpath('media')

LAST_SELFIE = MEDIA_ROOT.joinpath('last_selfie.jpg')
SCHOOL_PHOTO = MEDIA_ROOT.joinpath('school_photo.jpg')

GPT_VOICE = MEDIA_ROOT.joinpath('gpt_voice.ogg')
SQL_VOICE = MEDIA_ROOT.joinpath('sql_voice.ogg')
LOVE_VOICE = MEDIA_ROOT.joinpath('love_voice.ogg')

PHOTO_PATH = {'last_selfie': LAST_SELFIE, 'school_photo': SCHOOL_PHOTO}

VOICE_PATH = {
    'gpt_voice': GPT_VOICE,
    'sql_voice': SQL_VOICE,
    'love_voice': LOVE_VOICE,
}

PHOTO_CALLBACK = {
    'last_selfie': 'Последнее селфи',
    'school_photo': 'Фото из школы',
}

VOICE_CALLBACK = {
    'gpt_voice': 'Про Chat GPT',
    'sql_voice': 'Про SQL и NoSQL',
    'love_voice': 'История первой любви',
}
