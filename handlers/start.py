from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
        "🐠 ربات آکواریومی با موفقیت اجرا شد!\n\nبه زودی کلی امکانات اضافه می‌کنیم 😉"
    )
