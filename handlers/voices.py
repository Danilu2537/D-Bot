from aiogram import types

from handlers.commands import get_interests, get_photos, get_repo, get_voices
from handlers.recognizer import MessageRecognizer
from loader import dp
from settings import VOICE_COMPRASION

message_recognizer: MessageRecognizer = MessageRecognizer()

func_comprasion: dict[str, callable] = {
    'interests': get_interests,
    'photos': get_photos,
    'voices': get_voices,
    'repo': get_repo,
}


@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def get_voice(message: types.Message) -> None:
    """
    Handle voice messages in the chat.

    Args:
        message (types.Message): The incoming message object.

    Returns:
        None
    """
    # Recognize the voice message
    text: str = await message_recognizer.recognize_voice(message)

    # Compare the recognized words with pre-defined values
    for key, value in VOICE_COMPRASION.items():
        for word in text.split():
            if word in value:
                # Call the corresponding function based on the matched word
                await func_comprasion[key](message)
                return

    # If no matching word found, send a default message
    await message.answer('Ой, я пока не умею этого делать 🙈')
