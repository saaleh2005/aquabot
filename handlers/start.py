from aiogram import Router
from aiogram.types import Message
from db.database import cursor, conn

start_router = Router()

@start_router.message(commands=["start"])
async def start(message: Message):
    user_id = message.from_user.id

    cursor.execute(
        "INSERT OR IGNORE INTO users (tg_id, score) VALUES (?, 0)",
        (user_id,)
    )
    conn.commit()

    await message.answer("🐠 خوش آمدید! ربات آکواریومی آماده است.")
