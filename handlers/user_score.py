from aiogram import Router
from aiogram.types import Message
from db.database import cursor

user_score_router = Router()

@user_score_router.message(commands=["user_score"])
async def user_score(message: Message):
    user_id = message.from_user.id

    cursor.execute(
        "SELECT score FROM users WHERE tg_id = ?",
        (user_id,)
    )
    result = cursor.fetchone()

    if not result:
        await message.answer("❌ هنوز امتیازی نداری. اول در کوییز شرکت کن 😉")
        return

    score = result[0]

    await message.answer(
        f"🏆 امتیاز فعلی شما: {score}\n"
        "🎯 برای افزایش امتیاز در کوییز شرکت کن!"
  )
