from aiogram import Router, F
from aiogram.types import Message
from db.database import cursor

search_router = Router()

@search_router.message(F.text.len() > 2)
async def search_handler(message: Message):
    text = message.text.strip()

    # اگر دستور بود، ردش کن
    if text.startswith("/"):
        return

    cursor.execute("""
        SELECT id, title FROM articles
        WHERE title LIKE ? OR content LIKE ? OR tags LIKE ?
    """, (f"%{text}%", f"%{text}%", f"%{text}%"))

    results = cursor.fetchall()

    if not results:
        await message.answer("🔍 نتیجه‌ای پیدا نشد.")
        return

    response = "🔍 نتایج جستجو:\n\n"
    for art_id, title in results:
        response += f"📘 /article_{art_id} — {title}\n"

    await message.answer(response)
