import sqlite3

def init_db():
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        analysis TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_email(text, analysis):
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO emails (text, analysis) VALUES (?, ?)", (text, analysis))

    conn.commit()
    conn.close()