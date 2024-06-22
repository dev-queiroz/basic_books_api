import sqlite3

conn = sqlite3.connect('books.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL
);
""")

conn.commit()
conn.close()
