import sqlite3

conn = sqlite3.connect("aqua.db")
cursor = conn.cursor()

# کاربران
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tg_id INTEGER UNIQUE,
    username TEXT,
    score INTEGER DEFAULT 0
)
""")

# مقالات
cursor.execute("""
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    tags TEXT
)
""")

# سوالات کوییز
cursor.execute("""
CREATE TABLE IF NOT EXISTS quiz_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    option_a TEXT,
    option_b TEXT,
    option_c TEXT,
    option_d TEXT,
    correct_option TEXT
)
""")

# سوالات تستی
cursor.execute("""
INSERT OR IGNORE INTO quiz_questions
(id, question, option_a, option_b, option_c, option_d, correct_option)
VALUES
(1, 'بهترین دما برای آکواریوم گیاهی کدام است؟',
 '۱۸–۲۰ درجه', '۲۲–۲۶ درجه', '۳۰–۳۲ درجه', '۱۵–۱۷ درجه', 'b'),
(2, 'سیفون آب معمولاً هر چند وقت یک‌بار انجام می‌شود؟',
 'هر روز', 'هر هفته', 'هر ۶ ماه', 'هر سال', 'b')
""")

# مقالات تستی
cursor.execute("""
INSERT OR IGNORE INTO articles (id, title, content, tags) VALUES
(1, 'شروع آکواریوم برای مبتدی‌ها',
 'در این مقاله یاد می‌گیریم چگونه یک آکواریوم را از صفر راه‌اندازی کنیم...',
 '#مبتدی #راه_اندازی'),
(2, 'سیفون آب چیست؟',
 'سیفون کردن یعنی تعویض بخشی از آب آکواریوم برای حفظ کیفیت آب...',
 '#نگهداری #سیفون')
""")

conn.commit()
