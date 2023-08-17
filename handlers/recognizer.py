import os

import speech_recognition as sr
from aiogram import types

from loader import bot
from settings import MEDIA_ROOT


class MessageRecognizer:
    def __init__(self):
        self._r: sr.Recognizer = sr.Recognizer()

    async def recognize_voice(self, message: types.Message) -> str:
        """
        Downloads the voice message from the given message object,
        transforms the downloaded audio file from ogg to wav format,
        and recognizes the text from the transformed audio file.

        Args:
            message (types.Message): The message object containing the
            voice message.

        Returns:
            str: The recognized text from the voice message.
        """
        # Download voice message as ogg file
        downloaded_ogg: str = await self._download_voice(message)

        # Transform ogg file to wav format
        audio_wav: str = self._transformate_ogg_to_wav(downloaded_ogg)

        # Recognize text from wav file
        text: str = self._recognize_audio(audio_wav)

        # Delete downloaded files
        os.remove(downloaded_ogg)
        os.remove(audio_wav)

        return text

    async def _download_voice(self, message: types.Message) -> str:
        """
        Downloads the voice file from the given message and
        returns the path where it is saved.

        Args:
            message (types.Message): The message containing the voice file.

        Returns:
            str: The path where the voice file is saved.
        """
        file: types.File = await message.voice.get_file()
        path: str = f'{MEDIA_ROOT}/{message.chat.id}.ogg'
        await bot.download_file(file.file_path, path)
        return path

    def _recognize_audio(self, path: str) -> str:
        """
        Recognizes speech from an audio file.

        Args:
            path (str): The path to the audio file.

        Returns:
            str: The recognized text.
        """
        with sr.AudioFile(path) as source:
            audio_data: sr.AudioData = self._r.listen(source)
            text: str = self._r.recognize_google(audio_data, language='ru_RU')
        return text

    def _transformate_ogg_to_wav(self, path_ogg: str) -> str:
        """
        Transforms an OGG audio file to WAV format using FFmpeg.

        Args:
            path_ogg (str): The path to the OGG audio file.

        Returns:
            str: The path to the converted WAV audio file.
        """
        # Generate the path for the WAV file by replacing the file extension
        path_wav: str = path_ogg[:-4] + '.wav'

        # Use FFmpeg to convert the OGG file to WAV
        os.system(f'ffmpeg -i {path_ogg} {path_wav}')

        return path_wav
