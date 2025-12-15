from aiogram import Router
from aiogram.types import Message
from db.database import cursor

search_router = Router()


@search_router.message()
async def search_handler(message: Message):
    if not message.text:
        return

    text = message.text.strip()

    # ignore commands
    if text.startswith("/"):
        return

    # ignore quiz answers
    if text.lower() in ("a", "b", "c", "d"):
        return

    # ignore short messages
    if len(text) < 3:
        return

    cursor.execute(
        "SELECT id, title FROM articles WHERE title LIKE ? OR content LIKE ? OR tags LIKE ?",
        (f"%{text}%", f"%{text}%", f"%{text}%")
    )

    results = cursor.fetchall()

    if not results:
        await message.answer("🔍 نتیجه‌ای پیدا نشد.")
        return

    response = "🔍 نتایج جستجو:\n\n"
    for art_id, title in results:
        response += f"📘 /article_{art_id} — {title}\n"

    await message.answer(response)
