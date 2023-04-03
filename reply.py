from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

st = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Начать анкетирование!")]
    ],
    resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Нажмите 'Начать анкетирование!'",
    selective=True)

nexT = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Назад"), KeyboardButton(text="Далее")]], resize_keyboard=True, one_time_keyboard=True,
    selective=True)

lq = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Закончить анкетирование")]], resize_keyboard=True, one_time_keyboard=False,
    selective=True)

answer = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Да"),
                                        KeyboardButton(text="Нет")]], resize_keyboard=True, one_time_keyboard=False)
