import asyncpg
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from config import config
from bot.handlers import user, common, setup_routers
from bot.utils.commands import set_commands

import asyncio
import logging


async def start_bot(bot: Bot):
    await set_commands(bot)
    # await bot.send_message(config.bot.admin_ids, text='Бот запущен!')


async def stop_bot(bot: Bot):
    print('Stopped')
    # await bot.send_message(config.bot.admin_ids, text='Бот остановлен!')


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.config.bot.token)
    # pool_connect = await create_pool()
    # storage = await asyncpg.connect(pool_connect)
    dp = Dispatcher()

    # dp.update.message.register(DbSession(pool_connect))
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    router = setup_routers()
    dp.include_router(router)

    # dp.message.register(sender.get_sender, Command(commands='sender', magic=F.args),
    #                     F.chat.id in config.bot.admin_ids)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('--- Bot stopped ---')