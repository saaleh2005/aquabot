from aiogram import Router
from aiogram.types import Message
from db.database import cursor

stats_router = Router()

@stats_router.message(commands=["user_score"])
async def user_score(message: Message):
    user_id = message.from_user.id

    cursor.execute(
        "SELECT score FROM users WHERE tg_id = ?",
        (user_id,)
    )
    row = cursor.fetchone()

    score = row[0] if row else 0

    await message.answer(f"🏆 امتیاز شما: {score}")


@stats_router.message(commands=["quiz_stats"])
async def quiz_stats(message: Message):
    cursor.execute(
        "SELECT tg_id, score FROM users ORDER BY score DESC LIMIT 10"
    )
    rows = cursor.fetchall()

    if not rows:
        await message.answer("❌ هنوز داده‌ای وجود ندارد.")
        return

    text = "🏆 Top 10 کاربران کوییز:\n\n"
    for i, (tg_id, score) in enumerate(rows, start=1):
        text += f"{i}️⃣ کاربر {tg_id} — {score} امتیاز\n"

    await message.answer(text)
