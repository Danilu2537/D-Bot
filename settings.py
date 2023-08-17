from pathlib import Path
from typing import Dict

from envparse import env

BASE_DIR: Path = Path(__file__).resolve().parent

ENV_PATH: Path = BASE_DIR.joinpath('.env')
if ENV_PATH.is_file():
    env.read_envfile(ENV_PATH)

REPO_URL: str = 'https://github.com/Danilu2537/D-Bot'
BOT_TOKEN: str = env.str('BOT_TOKEN')

COMMANDS: Dict[str, str] = {
    'photos': 'Мои фотографии 😎',
    'interests': 'Мое главное увлечение 🤓',
    'voices': 'Мои голосовые 🤩',
    'repo': 'Репозиторий этого бота 📚',
    'cancel': 'Отмена 🚫',
}

START_MESSAGE: str = (
    'Привет 🙃\n Я Данила. Давай познакомимся! '
    'Выбери, что бы ты хотел узнать? '
    'Или скажи голосом, я пойму 😎'
)
INTERESTS_MESSAGE: str = (
    'Я с удовольствием занимаюсь программированием и автоматизацией 😄, '
    'но также обожаю играть в видеоигры 🎮 и занимаюсь музыкой 🎵. '
    'Кроме того, я с радостью преподаю, чтобы делиться своим опытом и '
    'помогать другим в их путешествии в программировании 🎓✨.'
)

VOICE_COMPRASION: Dict[str, list] = {
    'photos': [
        'фото',
        'фотографии',
        'фотография',
        'фоточка',
        'фоточки',
        'фоточек',
    ],
    'interests': ['увлечение', 'интерес', 'хобби', 'интересы', 'увлечения'],
    'voices': ['голос', 'голосовое', 'голосовой', 'голоса', 'голосовые'],
    'repo': ['репо', 'репа', 'репу', 'репозиторий', 'репозитория'],
}

MEDIA_ROOT: Path = BASE_DIR.joinpath('media')

LAST_SELFIE: Path = MEDIA_ROOT.joinpath('last_selfie.jpg')
SCHOOL_PHOTO: Path = MEDIA_ROOT.joinpath('school_photo.jpg')

GPT_VOICE: Path = MEDIA_ROOT.joinpath('gpt_voice.ogg')
SQL_VOICE: Path = MEDIA_ROOT.joinpath('sql_voice.ogg')
LOVE_VOICE: Path = MEDIA_ROOT.joinpath('love_voice.ogg')

PHOTO_PATH: Dict[str, Path] = {
    'last_selfie': LAST_SELFIE,
    'school_photo': SCHOOL_PHOTO,
}

VOICE_PATH: Dict[str, Path] = {
    'gpt_voice': GPT_VOICE,
    'sql_voice': SQL_VOICE,
    'love_voice': LOVE_VOICE,
}

PHOTO_CALLBACK: Dict[str, str] = {
    'last_selfie': 'Последнее селфи',
    'school_photo': 'Фото из школы',
}

VOICE_CALLBACK: Dict[str, str] = {
    'gpt_voice': 'Про Chat GPT',
    'sql_voice': 'Про SQL и NoSQL',
    'love_voice': 'История первой любви',
}
