import sqlite3

conn = sqlite3.connect("aqua.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tg_id INTEGER UNIQUE,
    username TEXT,
    score INTEGER DEFAULT 0
)
""")

conn.commit()
