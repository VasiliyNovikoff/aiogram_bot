from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter, Text
from aiogram.types import Message


# api_token, полученный у bot_father
API_TOKEN: str = '#'

# Создаём объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Этот фильтр будет проверять наличие в тексте целых, неотрицательных чисел
# и передавать их в хэндлер
class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers: list = []
        # разрезаем текст по словам и проверяем на числа
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',', '').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
        if numbers:
            return {'numbers': numbers}
        return False


# Хэндлер, который реагирует на текст, начинающийся с "найди числа"
@dp.message(Text(startswith='найди числа', ignore_case=True), NumbersInMessage())
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(text=f'Нашёл {str(", ".join(str(num) for num in numbers))}')


# Хэндлер, срабатывающий, если нет чисел в тексте
@dp.message(Text(startswith='найди числа', ignore_case=True))
async def process_if_not_numbers(message: Message):
    await message.answer('Не удалось найти :(')


if __name__ == '__main__':
    dp.run_polling(bot)
