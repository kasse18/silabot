import requests
from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

router = Router()


@router.message(F.text != "/start", StateFilter(None))
async def question(message: Message, state: FSMContext):
    msg = message.text
    print(msg)
    r = requests.post('http://194.67.84.96:8999/get_answer', json={"query": msg, "chat_id": str(message.chat.id), "user_id": str(message.chat.id)}).json()
    print(r)
    await message.answer(
        text=f"{r["answer"]}"
    )