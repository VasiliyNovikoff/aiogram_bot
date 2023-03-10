from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router
from keyboards.set_menu import set_main_menu


router: Router = Router()


# Этот хэндлер будет срабатывать на команду /delmenu
# и удалять кнопку меню
@router.message(Command(commands='delmenu'))
async def del_main_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer('Кнопка "Menu" удалена. Перезапустите приложение')


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('Hello!')


@router.message(Command(commands='menu'))
async def process_menu_command(message: Message, bot: Bot):
    await message.answer('Menu активировано. Перезапустите приложение')
    await set_main_menu(bot)
