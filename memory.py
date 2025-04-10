import sqlite3
from datetime import datetime

class FuffyMemory:
    def __init__(self, db_path="fuffy.sqlite3"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT,
                content TEXT,
                timestamp TEXT
            )
        """)
        self.conn.commit()

    def save_dialogue(self, role, content):
        self.conn.execute(
            "INSERT INTO memory (role, content, timestamp) VALUES (?, ?, ?)",
            (role, content, datetime.now().isoformat())
        )
        self.conn.commit()

    def get_last_context(self, limit=10):
        cursor = self.conn.execute(
            "SELECT role, content FROM memory ORDER BY id DESC LIMIT ?", (limit,)
        )
        messages = reversed(cursor.fetchall())
        return "\n".join([f"{role.capitalize()}: {text}" for role, text in messages])