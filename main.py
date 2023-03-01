from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message
import os
import dotenv


# функция для получения переменных из файла .env в окружение
# в качестве переменной - путь к файлу .env (если в одной папке с исполняемых файлом - можно не указывать)
dotenv.load_dotenv()

# api_token, полученный у bot_father
API_TOKEN: str = os.getenv('BOT_TOKEN')

# Создаём объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Список с id администраторов бота
admin_ids: list[int] = [409264813]


# Собственный фильтр, проверяющий на принадлежность к admin_ids
class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in admin_ids


# Этот хэндлер будет обрабатывать апдейт, если он от админа
@dp.message(IsAdmin(admin_ids))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')


# Этот хэндлер будет обрабатывать апдейт, если он не от админа
@dp.message()
async def answer_if_not_admins_update(message: Message):
    print(message.json(exclude_none=True, indent=4))
    await message.answer(text='Вы не админ')


if __name__ == '__main__':
    dp.run_polling(bot)
