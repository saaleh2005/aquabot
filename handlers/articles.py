from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from db.database import cursor

articles_router = Router()

@articles_router.callback_query(F.data == "articles")
async def show_articles(callback: CallbackQuery):
    cursor.execute("SELECT id, title FROM articles")
    articles = cursor.fetchall()

    if not articles:
        await callback.message.answer("📚 هنوز مقاله‌ای وجود ندارد.")
        await callback.answer()
        return

    text = "📚 لیست مقالات:\n\n"
    for art_id, title in articles:
        text += f"🔹 /article_{art_id} — {title}\n"

    await callback.message.answer(text)
    await callback.answer()


@articles_router.message(lambda msg: msg.text.startswith("/article_"))
async def read_article(message: Message):
    art_id = message.text.replace("/article_", "")
    cursor.execute(
        "SELECT title, content FROM articles WHERE id = ?",
        (art_id,)
    )
    article = cursor.fetchone()

    if not article:
        await message.answer("❌ مقاله پیدا نشد")
        return

    title, content = article
    await message.answer(f"📘 {title}\n\n{content}")
