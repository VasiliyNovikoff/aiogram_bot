from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Text, Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
    Message, CallbackQuery, BotCommand, InputMediaVideo, InputMediaAudio, \
    InputMediaPhoto, InputMediaDocument, InputMedia
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
import random
from aiogram.exceptions import TelegramBadRequest

from config_data.config import Config, load_config
from handlers import user_handlers
from keyboards.create_inline_kb import create_inline_kb
from lexicon.lexicon_ru import BUTTONS
import pprint


config: Config = load_config()

# Инициализируем бот и диспетчер
bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()


file_dict: dict = {
    'audio': '🎶 Аудио',
    'text': '📃 Текст',
    'photo': '🖼 Фото',
    'video_note': '🎬 Видео',
    'video': '🎬 Видео',
    'document': '📑 Документ',
    'voice': '📢 Голосовое сообщение',
    'text_1': 'Это обыкновенное текстовое сообщение, его можно легко отредактировать другим '
              'текстовым сообщением, но нельзя отредактировать сообщением с медиа.',
    'text_2': 'Это тоже обыкновенное текстовое сообщение, которое можно заменить на другое текстовое '
              'сообщение через редактирование.',
    'video_note_id': ['DQACAgIAAxkBAAIDn2QV3EqTph-_Fzwmgn5OBobj4zqNAAIzLQACtKWxSEbJs1S2CmmSLwQ',
                      'DQACAgIAAxkBAAIDoGQV3MZAEWmaIHBvATQ5ymyPc7_CAAJSLgACtKWxSHS8lHJLSCzKLwQ'],
    'photo_id': ['AgACAgIAAxkBAAIDoWQV3PY53uvEezSkZ0XWScfxXGF9AAJJxjEbtKWxSD3ZGAoOHpEbAQADAgADcwADLwQ',
                 'AgACAgIAAxkBAAIDomQV3ViA8w16bfwdmeZJudN_3pz1AAIzxzEbtKWxSOYoEe7mK5t6AQADAgADbQADLwQ'],
    'voice_id': ['AwACAgIAAxkBAAIDpGQV3aT0JV_keDcC0cpCK4vZecyDAAJULgACtKWxSJfjLIaBX6dfLwQ',
                 'AwACAgIAAxkBAAIDpmQV3eR_qQL68_WMKXGb2INifmtzAAJXLgACtKWxSOt1vgiBjuURLwQ'],
    'document_id': ['BQACAgIAAxkBAAIDp2QV3hODjpw8gWEdYM1RsFjVgIO6AAJZLgACtKWxSFQzXyRMEpqwLwQ',
                 'BQACAgIAAxkBAAIDqGQV3j-QInTv5gdxvmJVFnXw1LAkAAJbLgACtKWxSBxxsSmjnGXeLwQ'],
    'audio_id': ['CQACAgIAAxkBAAIDqWQV3oXq0SNooBPY-Sm1ledmYzE8AAJcLgACtKWxSHGeEHCCxhvhLwQ',
                 'CQACAgIAAxkBAAIDqmQV3q-aa2MSpeXySZwmbfV-1pP6AAJfLgACtKWxSISaPzU5aLMwLwQ'],
    'video_id': ['BAACAgIAAxkBAAID1mQYjjyXU97Ih9RkjSOgxHhkxpGnAAJ-LwAC4YfJSGHilVAFakNJLwQ',
                 'BAACAgIAAxkBAAID2GQYj-_ET8XoGZfuzk4lbks2-akJAAKULwAC4YfJSKsFmby7fGZTLwQ'],
    'video_unique_id': ['AgADfi8AAuGHyUg',
                        'AgADlC8AAuGHyUg']}


# Функция для генерации клавиатуры с инлайн-кнопками
def get_markup(width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []

    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=file_dict[button] if button in file_dict else button,
                callback_data=button))

    if kwargs:
        for text, button in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()


# Этот хэндлер будет срабатывать на команду /start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    markup = get_markup(2, 'photo')
    await message.answer_photo(photo=file_dict['photo_id'][0],
                               caption='Это фото 1',
                               reply_markup=markup)


# Этот хэндлер будет срабатыть на нажатие инлайн-кнопки
@dp.callback_query(Text(text=['text',
                              'audio',
                              'photo',
                              'video_note',
                              'voice',
                              'document',
                              'video']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = get_markup(2, 'photo', 'audio')
    try:
        await bot.edit_message_media(chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     media=InputMediaAudio(caption='Это аудио 1',
                                                           media=file_dict['audio_id'][0]),
                                     reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     media=InputMediaAudio(media=file_dict['audio_id'][1],
                                                           caption='Это аудио 2'),
                                     reply_markup=markup)


# Этот хэндлер будет срабатывать на все остальные сообщения
@dp.message()
async def send_echo(message: Message):
    await message.answer(text='Не понимаю :(')
    print(message.json(indent=4, exclude_none=True))


if __name__ == '__main__':
    dp.run_polling(bot)
