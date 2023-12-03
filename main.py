import asyncio
from config import SECRET_TOKEN
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command
from aiogram.filters import CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import StateFilter

import logging
import random
from random_fox import fox
from handlers import career_choiсe



#

#
#
# # Хэндлер на команду /start
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Привет 😊", reply_markup=keyword1)
#
#
# # Хэндлер на команду /run
# @dp.message(Command("run"))
# async def cmd_run(message: types.Message):
#     await message.answer("Привет 😊\nОтправь своё фото", reply_markup=keyword2)
#
#
# # Хэндлер на команду /info
# @dp.message(Command("info"))
# async def cmd_info(message: types.Message):
#     number = random.randint(1, 7)
#     await message.answer("Я тестовый бот")
#     await message.answer(f"Твоё число {number}")
#
#
# # Хэндлер на кнопку "Отправит фото
# @dp.message(F.text == 'Отправить фото')
# async def cmd_foto(message: types.Message, state: FSMContext):
#     # await ClientStateGroup.photo.set()
#     await state.set_state(ClientStateGroup.photo)
#     await message.answer(f"Теперь жду твоё фото 😊")
#
#
# @dp.message(lambda message: not message.photo, state=state.set_state(ClientStateGroup.photo))
# async def check_photo(message: types.Message):
#     await message.reply('Это не фото')
#
#
#
# # Хэндлер на команду /fox
# @dp.message(F.text == 'Показать лису')
# @dp.message(Command("fox"))
# async def cmd_fox(message: types.Message):
#     img_fox = fox()
#     await message.answer(f"Держи лису 😊")
#     await bot.send_photo(message.from_user.id, photo=img_fox)
#
#
# # Хэндлер на сообщения
# @dp.message(F.text)
# async def msg_echo(message: types.Message):
#     print(message.text)
#     name = message.chat.first_name
#     if "привет" in message.text.lower():
#         await message.answer(f"Привет, {name}")
#     elif "пока" in message.text.lower():
#         await message.answer(f"Пока, {name}")
#     elif "ты кто" in message.text.lower():
#         await message.answer(f"<b>Я бот</b> {name}")
#     elif "ура" in message.text.lower():
#         await message.answer("<i>Ура-ура</i>!!!!!!!!!")
#     else:
#         await message.answer("<s>Я тебя не понимаю</s>")


async def main():
    logging.basicConfig(level=logging.INFO)

    # Объект бот
    bot = Bot(token=SECRET_TOKEN, parse_mode='HTML')

    dp = Dispatcher()

    dp.include_router(career_choiсe.router)
    # dp.include_router(common.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())