from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher
from config_data.config import load_config
from aiogram.filters import CommandStart, Command
from aiogram.types.web_app_info import WebAppInfo


config = load_config('/')
bot_token = config.tg_bot.token

bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher()

################
# ОТДЕЛЬНЫЙ БЛОК КНОПОК И ДОБАВЛЕНИЯ ИХ В КЛАВИАТУРУ

# Инициализируем билдер
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаём кнопки
contact_btn: KeyboardButton = KeyboardButton(text='Поделиться контактом',
                                             request_contact=True)
geo_btn: KeyboardButton = KeyboardButton(text='Отправить гео позицию',
                                         request_location=True)
poll_btn: KeyboardButton = KeyboardButton(text='Создать опрос',
                                          request_poll=KeyboardButtonPollType(type='regular'))
quiz_btn: KeyboardButton = KeyboardButton(text='Создать викторину',
                                          request_poll=KeyboardButtonPollType(type='quiz'))

# Добавляем кнопки в билдер методом row
kb_builder.row(contact_btn, geo_btn, poll_btn, quiz_btn, width=1)

# Создаём объект клавиатуры (контакт, гео, опсрос, виктрорина)
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True,
                                                     one_time_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/btn"
@dp.message(Command(commands=['btn']))
async def process_btn_command(message: Message):
    await message.answer('Экперименты с кнопками',
                         reply_markup=keyboard)

###############
# ОТДЕЛЬНЫЙ БЛОК КНОПОК И ДОБАВЛЕНИЯ ИХ В КЛАВИАТУРУ

# Кнопка для web app
web_app_btn: KeyboardButton = KeyboardButton(text='Start Web App',
                                             web_app=WebAppInfo(url='https://stepik.org/'))

# Клавиатура для web app
web_app_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(text='Start Web App',
                                                            keyboard=[[web_app_btn]],
                                                            resize_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('Экспериментируем с веб приложением',
                         reply_markup=web_app_keyboard)

###############
# ОТДЕЛЬНЫЙ БЛОК КНОПОК И ДОБАВЛЕНИЯ ИХ В КЛАВИАТУРУ
# параметр input_field_placeholder

# Инициализируем билдер
kb_builder_2: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаём список кнопок
buttons: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i+1}') for i in range(10)]

# Добавляем кнопки в билдер
kb_builder_2.add(*buttons)

# Сообщаем билдеру, сколько хотим видеть кнопок в первом и втором ряду
kb_builder_2.adjust(1, 3, repeat=True)

# Создаём объект клавиатуры
placeholder_example_kb: ReplyKeyboardMarkup = kb_builder_2.as_markup(
                                                resize_keyboard=True,
                                                input_field_placeholder='Текст, который будет в поле ввода')


# Этот хэндлер будет срабатывать на команду "/placeholder" - надписи нет
@dp.message(Command(commands=['placeholder']))
async def process_placeholder_command(message: Message):
    await message.answer(text='Экспериментируем с полем placeholder',
                         reply_markup=placeholder_example_kb)


ph_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[buttons[:2], buttons[2:]],
                                                 resize_keyboard=True,
                                                 input_field_placeholder='Текст, который будет в поле ввода')


# Этот хэндлер будет срабатывать на команду "/ph"
@dp.message(Command(commands=['ph']))
async def process_placeholder_command(message: Message):
    await message.answer(text='Экспериментируем с полем placeholder',
                         reply_markup=ph_kb)

###############

if __name__ == '__main__':
    dp.run_polling(bot)
