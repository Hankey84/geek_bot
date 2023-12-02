import asyncio
from config import SECRET_TOKEN
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.filters import CommandObject
import logging
import random
from keyboard import keyword1
from random_fox import fox


logging.basicConfig(level=logging.INFO)

# Объект бот
bot = Bot(token=SECRET_TOKEN, parse_mode="HTML")

dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет 😊!", reply_markup=keyword1)


# Хэндлер на команду /info
@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    number = random.randint(1, 7)
    await message.answer("Я тестовый бот")
    await message.answer(f"Твоё число {number}")

# Хэндлер на команду /fox
@dp.message(F.text == 'Показать лису')
@dp.message(Command("fox"))
async def cmd_start(message: types.Message):
    img_fox = fox()
    await message.answer(f"Держи лису 😊")
    await bot.send_photo(message.from_user.id, photo=img_fox)

# Хэндлер на сообщения
@dp.message(F.text)
async def msg_echo(message: types.Message):
    print(message.from_user.id) # Кто в чат вошел, идентификатор

    name = message.chat.first_name
    if "привет" in message.text.lower():
        await message.answer(f"Привет, {name}")
    elif "пока" in message.text.lower():
        await message.answer(f"Пока, {name}")
    elif "ты кто" in message.text.lower():
        await message.answer(f"Я бот {name}")
    elif "ура" in message.text.lower():
        await message.answer("Ура-ура!!!!!!!!!")
    else:
        await message.answer("Я тебя не понимаю")



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())