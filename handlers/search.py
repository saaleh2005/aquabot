from aiogram import Router
from aiogram.types import Message
from db.database import cursor

search_router = Router()

@search_router.message()
async def search_handler(message: Message):
    if not message.text:
        return

    text = message.text.strip()

    if text.startswith("/"):
        return

    if text.lower() in ("a", "b", "c", "d"):
        return

    if len(text) < 3:
        return

    cursor.execute(
        "SELECT id, title FROM articles WHERE title LIKE ? OR content LIKE ? OR tags LIKE ?",
        (f"%{text}%", f"%{text}%", f"%{text}%")
    )

    rows = cursor.fetchall()

    if not rows:
        await message.answer("🔍 نتیجه‌ای پیدا نشد.")
        return

    msg = "🔍 نتایج جستجو:\n\n"
    for art_id, title in rows:
        msg += f"📘 /article_{art_id} — {title}\n"

    await message.answer(msg)
