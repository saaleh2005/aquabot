from aiogram import Router
from aiogram.types import Message
from db.database import cursor

search_router = Router()

@search_router.message()
async def search_handler(message: Message):
    query = message.text.strip()

    # دستورات رو رد کن
    if query.startswith("/"):
        return

    cursor.execute("""
    SELECT id, title FROM articles
    WHERE title LIKE ? OR content LIKE ? OR tags LIKE ?
    """, (f"%{query}%", f"%{query}%", f"%{query}%"))

    results = cursor.fetchall()

    if not results:
        await message.answer("🔍 نتیجه‌ای پیدا نشد.")
        return

    text = "🔍 نتایج جستجو:\n\n"
    for art_id, title in results:
        text += f"📘 /article_{art_id} — {title}\n"

    await message.answer(text)
