import sqlite3
import os

DB_PATH = os.path.join("data", "quotes.db")

def get_connection():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS quotes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quote_text TEXT NOT NULL,
                author TEXT NOT NULL,
                used INTEGER DEFAULT 0
            )
        """)
        conn.commit()

def get_next_quote():
    with get_connection() as conn:
        result = conn.execute("SELECT * FROM quotes WHERE used = 0 LIMIT 1").fetchone()
        return result

def mark_quote_as_used(quote_id):
    with get_connection() as conn:
        conn.execute("UPDATE quotes SET used = 1 WHERE id = ?", (quote_id,))
        conn.commit()

def add_quote(text, author):
    with get_connection() as conn:
        conn.execute("INSERT INTO quotes (quote_text, author) VALUES (?, ?)", (text, author))
        conn.commit()
