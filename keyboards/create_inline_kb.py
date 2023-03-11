"""
Функция для создания инлайн-клавиатуры 'на лету'
*args - ключи к словарю, если они есть
**kwargs - готовый словарь с кнопками и текстом

Пример:
keyboard_inline_1 = create_inline_kb(2, 'but_1', 'but_3', 'but_7')
keyboard_inline_2 = create_inline_kb(3, last_btn='Пока!', **BUTTONS)
 с именованными аргументами:
keyboard_inline_3 = create_inline_kb(1, btn_email='Email',
                                        btn_tel='Телефон',
                                        btn_website='Web-сайт',
                                        btn_vk='VK',
                                        btn_tg_bot='Наш телеграм-бот'))
"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_BUTTONS


# Функция для генерации инлайн-клавиатуры "на лету"
def create_inline_kb(width: int,
                     *args,
                     last_btn: str | None = None,
                     **kwargs) -> InlineKeyboardMarkup:
    # Инициализируем билдер инлайн-клавиатуры
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON_BUTTONS[button] if button in LEXICON_BUTTONS else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    # Распаковываем список кнопок в билдер методом row с параметром width
    kb_builder.row(*buttons, width=width)

    # Добавляем последнюю кнопку в билдер, если она передана в функцию
    if last_btn:
        kb_builder.row(InlineKeyboardButton(
            text=last_btn,
            callback_data='last_btn'))

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()

