import json

from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, CallbackQuery
import requests


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    if message.text == '/start':
        await message.answer(
            "Добро пожаловать в бота поддержки компании СИЛА\n\nНапишите ваш вопрос и наш бот поддержки поможет вам"
        )
