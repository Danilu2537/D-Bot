import logging
import types

from aiogram import Dispatcher, executor

import settings
from loader import dp


async def on_startup(dispatcher: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        filename='bot.log',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )
    logging.info('Бот запущен')
    await dp.bot.set_my_commands(
        [
            types.BotCommand(*key_value)
            for key_value in settings.COMMANDS.items()
        ]
    )


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    executor.start_polling(dp, on_startup=on_startup)
