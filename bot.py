from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message)
from config_data.config import load_config
from aiogram.utils.keyboard import ReplyKeyboardBuilder


config = load_config('/')
bot_token = config.tg_bot.token

bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher()

# Инициализируем объект билдера
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаём список с кнопками
buttons_1: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i}') for i in range(1, 11)]

# Методами билдера добавляем в него кнопки (метод .row())
# kb_builder.row(*buttons_1, width=4)

# Распаковываем список кнопок методом add
kb_builder.add(*buttons_1)

# Сообщаем билдеру, сколько хотим видеть кнопок в первом и втором ряду
kb_builder.adjust(2, 1, repeat=True)

# Методом as_markup() передаем клавиатуру, где она требуется


# Этот хэндлер будет срабатывать на комманду /start и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая клавиатура получилась',
                         reply_markup=kb_builder.as_markup(resize_keyboard=True))


# Этот хэндлер будет срабатывать на ответ "Собак" и удалять клавиатуру
@dp.message(Text(text='Собак'))
async def process_dog_answer(message: Message):
    await message.answer(text='Несомнемненно, кошки боятся собак.\n'
                              'Но видили как они пугаются огурцов!')


# Этот хэндлер будет срабатывать на ответ "Огурцов" и удалять клавиатуру
@dp.message(Text(text='Огурцов'))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, кошки боятся больше огурцов, чем собак!')


if __name__ == '__main__':
    dp.run_polling(bot)
