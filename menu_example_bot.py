from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config_data.config import Config, load_config
from keyboards.set_menu import set_main_menu
from handlers import user_handlers


config: Config = load_config()

# Инициализируем бот и диспетчер
bot: Bot = Bot(token=config.tg_bot.token,
               parse_mode='HTML')
dp: Dispatcher = Dispatcher()


# Создаем асинхронную функцию
async def main():

    dp.include_router(user_handlers.router)

    # Настраиваем кнопку меню
    await set_main_menu(bot)

    await dp.start_polling(bot)


if __name__ == '__main__':
    main()
