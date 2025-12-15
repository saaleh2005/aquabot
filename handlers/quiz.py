import random
from aiogram import Router, F
from aiogram.types import CallbackQuery
from db.database import cursor, conn

quiz_router = Router()

@quiz_router.callback_query(F.data == "quiz")
async def start_quiz(callback: CallbackQuery):
    cursor.execute("SELECT * FROM quiz_questions ORDER BY RANDOM() LIMIT 1")
    q = cursor.fetchone()

    if not q:
        await callback.message.answer("❌ سوالی وجود ندارد.")
        await callback.answer()
        return

    q_id, question, a, b, c, d, correct = q

    text = (
        f"🎯 {question}\n\n"
        f"A️⃣ {a}\n"
        f"B️⃣ {b}\n"
        f"C️⃣ {c}\n"
        f"D️⃣ {d}\n\n"
        "جواب رو با A / B / C / D بفرست"
    )

    # ذخیره جواب صحیح موقتاً در پیام
    await callback.message.answer(text)
    await callback.answer()

    # ذخیره correct جواب برای استفاده بعدی
    quiz_router.correct_answer = correct.lower()
