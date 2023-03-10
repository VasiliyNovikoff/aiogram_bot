from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery

from config_data.config import Config, load_config
from handlers import user_handlers


config: Config = load_config()

# Инициализируем бот и диспетчер
bot: Bot = Bot(token=config.tg_bot.token,
               parse_mode='HTML')
dp: Dispatcher = Dispatcher()


btn_callback_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Коллбэк кнопка 1',
    callback_data='cb_btn_1_pressed')

btn_callback_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Коллбэк кнопка 2',
    callback_data='cb_btn_2_pressed')

keyboard_cb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[btn_callback_1], [btn_callback_2]])


# Этот хэндлер будет обрабатывать команду /start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки',
        reply_markup=keyboard_cb)


@dp.callback_query(Text(text='cb_btn_1_pressed'))
async def process_cb_btn_1_press(callback: CallbackQuery):
    print(callback.json(indent=4))
    await callback.answer()


if __name__ == '__main__':
    dp.run_polling(bot)
