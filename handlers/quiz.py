from aiogram import Router
from aiogram.types import CallbackQuery, Message
from db.database import cursor, conn

quiz_router = Router()

active_quiz = {}

@quiz_router.callback_query(lambda c: c.data == "quiz")
async def start_quiz(callback: CallbackQuery):
    cursor.execute("SELECT * FROM quiz_questions ORDER BY RANDOM() LIMIT 1")
    q = cursor.fetchone()

    if not q:
        await callback.message.answer("❌ سوالی وجود ندارد.")
        return

    q_id, question, a, b, c, d, correct = q
    user_id = callback.from_user.id

    active_quiz[user_id] = correct.lower()

    text = (
        f"🎯 {question}\n\n"
        f"A️⃣ {a}\n"
        f"B️⃣ {b}\n"
        f"C️⃣ {c}\n"
        f"D️⃣ {d}\n\n"
        "✍️ جواب را با A / B / C / D ارسال کنید"
    )

    await callback.message.answer(text)


@quiz_router.message()
async def check_answer(message: Message):
    if not message.text:
        return

    user_id = message.from_user.id

    if user_id not in active_quiz:
        return

    answer = message.text.strip().lower()

    if answer not in ("a", "b", "c", "d"):
        return

    correct = active_quiz[user_id]

    if answer == correct:
        cursor.execute(
            "UPDATE users SET score = score + 1 WHERE tg_id = ?",
            (user_id,)
        )
        conn.commit()
        await message.answer("✅ درست گفتی! +1 امتیاز 🎉")
    else:
        await message.answer(f"❌ اشتباه بود\n✅ جواب درست: {correct.upper()}")

    del active_quiz[user_id]
