from aiogram import Bot, Dispatcher
from aiogram.filters.callback_data import CallbackData
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           Message, CallbackQuery)
from aiogram.filters import CommandStart
from aiogram import F

from config_data.config import Config, load_config


config: Config = load_config()
BOT_TOKEN = load_config().tg_bot.token

# Инициализируем бот и диспетчер
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


# Создаем свой класс фабрики коллбэков, указывая префис,
# а также структуру callback_data
class GoodsCallbackFactory(CallbackData, prefix='goods', sep='|'):
    category_id: int
    subcategory_id: int
    item_id: int


# Создаем объекты кнопок с приминением фабрики коллбэков
button_1: InlineKeyboardButton = InlineKeyboardButton(text='Категория 1',
                                                      callback_data=GoodsCallbackFactory(
                                                          category_id=1,
                                                          subcategory_id=0,
                                                          item_id=0).pack())

button_2: InlineKeyboardButton = InlineKeyboardButton(text='Категория 2',
                                                      callback_data=GoodsCallbackFactory(
                                                          category_id=2,
                                                          subcategory_id=0,
                                                          item_id=0).pack())

# Создаем объект клавиатуры, добавляя в список списки с кнопками
markup: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_1], [button_2]])


# Этот хэндлер будет срабатывать на комманду /start
# и отправлять пользователю сообщение с клавиатурой
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая клавиатура',
                         reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие любой инлайн-кнопки
# и отправлять в чат форматированный ответ с данными из callback_data
@dp.callback_query(GoodsCallbackFactory.filter())
async def process_category_press(callback: CallbackQuery,
                                 callback_data: GoodsCallbackFactory):
    await callback.message.answer(
        text=f'Категория товаров: {callback_data.category_id}\n'
             f'Подкатегория товаров: {callback_data.subcategory_id}\n'
             f'Товар: {callback_data.item_id}')
    await callback.answer()


'''# Используем магический фильтр, чтобы поймать нажатие
# на кнопку Категория 1
@dp.callback_query(GoodsCallbackFactory.filter(F.category_id == 1))
async def process_category_press(callback: CallbackQuery,
                                 callback_data: GoodsCallbackFactory):
    await callback.message.answer(text=callback_data.pack())
    await callback.answer()'''


'''# Этот хэндлер будет срабатывать на нажатие любой инлайн кнопки
# и печатать объект в терминал
@dp.callback_query()
async def process_any_inline_button_press(callback: CallbackQuery):
    print(callback.json(indent=4, exclude_none=True))
    await callback.answer()'''


if __name__ == '__main__':
    dp.run_polling(bot)
