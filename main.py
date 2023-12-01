import asyncio
from config import SECRET_TOKEN
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.filters import CommandObject
import logging
import random


logging.basicConfig(level=logging.INFO)

# Объект бот
bot = Bot(token=SECRET_TOKEN)

dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет")


# Хэндлер на команду /info
@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    number = random.randint(1, 7)
    await message.answer("Я тестовый бот")
    await message.answer(f"Твоё число {number}")

# Хэндлер на эхо общение
@dp.message(F.text)
async def msg_echo(message: types.Message):
    await message.answer("Привет")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())