from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📚 مقالات", callback_data="articles"),
                InlineKeyboardButton(text="🌿 گیاهان", callback_data="plants")
            ],
            [
                InlineKeyboardButton(text="🎯 کوییز", callback_data="quiz"),
                InlineKeyboardButton(text="🔍 جستجو", callback_data="search")
            ]
        ]
    )
