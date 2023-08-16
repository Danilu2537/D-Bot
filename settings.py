from pathlib import Path

from envparse import env

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR.joinpath('.env')
if ENV_PATH.is_file():
    env.read_envfile(ENV_PATH)


BOT_TOKEN = env.str('BOT_TOKEN')

COMMANDS = {
    'photos': 'Мои фотографии 😎',
    'about': 'Обо мне 🙃',
    'interests': 'Мое главное увлечение 🤓',
    'voices': 'Мои голосовые 🤩',
    'repo': 'Репозиторий этого бота 📚',
    'cancel': 'Отмена 🚫',
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

MEDIA_ROOT = BASE_DIR.joinpath('media')

LAST_SELFIE = MEDIA_ROOT.joinpath('last_selfie.jpg')
SCHOOL_PHOTO = MEDIA_ROOT.joinpath('school_photo.jpg')

GPT_VOICE = MEDIA_ROOT.joinpath('gpt_voice.ogg')
SQL_VOICE = MEDIA_ROOT.joinpath('sql_voice.ogg')
LOVE_VOICE = MEDIA_ROOT.joinpath('love_voice.ogg')
