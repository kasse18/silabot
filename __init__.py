from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

start_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Кнопка1'
        )
    ],
    [
        KeyboardButton(
            text='Кнопка2'
        )
    ],
    [
        KeyboardButton(
            text='Кнопка3'
        ),
        KeyboardButton(
            text='Кнопка4'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


help_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Главное Меню'
        )
    ]
])


my_profile_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text=''
        )
    ]
])