from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
import logging
import asyncio

# Создание бота
API_TOKEN = '8440573082:AAEcp2MjTlseIKeFKfDD6I85-M5kW9UEz_I'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Логирование
logging.basicConfig(level=logging.INFO)

# Обработчик команд
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Я работаю!")

# Основная функция для запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
