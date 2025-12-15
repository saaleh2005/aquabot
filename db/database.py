import sqlite3

conn = sqlite3.connect("aqua.db")
cursor = conn.cursor()

# جدول کاربران
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tg_id INTEGER UNIQUE,
    username TEXT,
    score INTEGER DEFAULT 0
)
""")

# جدول مقالات
cursor.execute("""
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    tags TEXT
)
""")

# مقالات تستی (فقط یک بار اضافه می‌شوند)
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
