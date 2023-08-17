import logging
from typing import Dict

from aiogram import Dispatcher, executor, types

import handlers  # noqa: F401
import settings
from loader import dp


async def on_startup(dispatcher: Dispatcher) -> None:
    """
    Set up logging and set bot commands on startup.

    Args:
        dispatcher: The aiogram Dispatcher object.

    Returns:
        None
    """
    logging.basicConfig(
        level=logging.INFO,
        filename='bot.log',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )
    logging.info('Бот запущен')

    commands: Dict[str, str] = settings.COMMANDS
    bot_commands = [
        types.BotCommand(command, description)
        for command, description in commands.items()
    ]
    await dispatcher.bot.set_my_commands(bot_commands)


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    executor.start_polling(dp, on_startup=on_startup)
