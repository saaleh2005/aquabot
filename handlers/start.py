from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from db.database import cursor, conn
from keyboards.menu import main_menu

start_router = Router()

@start_router.message(Command("start"))
async def start_cmd(message: Message):
    tg_id = message.from_user.id
    username = message.from_user.username

    cursor.execute(
        "INSERT OR IGNORE INTO users (tg_id, username) VALUES (?, ?)",
        (tg_id, username)
    )
    conn.commit()

    await message.answer(
        "🐠 خوش اومدی!\n\nیکی از گزینه‌ها رو انتخاب کن 👇",
        reply_markup=main_menu()
    )
