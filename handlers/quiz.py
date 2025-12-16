from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from db.database import cursor, conn

quiz_router = Router()

active_quiz = {}

@quiz_router.callback_query(F.data == "quiz")
async def start_quiz(callback: CallbackQuery):
    cursor.execute("""
        SELECT id, question, option_a, option_b, option_c, option_d, correct_option
        FROM quiz_questions
        ORDER BY RANDOM()
        LIMIT 1
    """)
    q = cursor.fetchone()

    if not q:
        await callback.message.answer("❌ سوالی وجود ندارد.")
        await callback.answer()
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
        "✍️ جواب رو با A / B / C / D بفرست"
    )

    await callback.message.answer(text)
    await callback.answer()


@quiz_router.message(F.text.lower().in_(["a", "b", "c", "d"]))
async def check_answer(message: Message):
    user_id = message.from_user.id

    if user_id not in active_quiz:
        return

    answer = message.text.lower()
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
