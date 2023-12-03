from aiogram import types


button1 = types.KeyboardButton(text='Случайная лиса')
button2 = types.KeyboardButton(text='Шо попало')
button3 = types.KeyboardButton(text='/dice')

button4 = types.KeyboardButton(text='Отправить фото')
button5 = types.KeyboardButton(text='Закрыть')


kb1 = [
    [button1, button2, button3],

]

kb2 = [
    [button4, button5],

]

keyword1 = types.ReplyKeyboardMarkup(keyboard=kb1,
                                     resize_keyboard=True,
                                     )

keyword2 = types.ReplyKeyboardMarkup(keyboard=kb2,
                                     resize_keyboard=True,
                                     )


def make_row_keyboard(items: list[str]) -> types.ReplyKeyboardMarkup:
    row = [types.KeyboardButton(text=item) for item in items]
    return types.ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)