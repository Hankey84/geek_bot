from aiogram import types


button1 = types.KeyboardButton(text='Показать лису')
button2 = types.KeyboardButton(text='Информация')
button3 = types.KeyboardButton(text='/dice')


kb1 = [
    [button1, button2, button3],
    ]


keyword1 = types.ReplyKeyboardMarkup(keyboard=kb1)