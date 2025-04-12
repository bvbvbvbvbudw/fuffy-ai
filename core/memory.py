import sqlite3
from datetime import datetime

class FuffyMemory:
    def __init__(self, db_path="core/fuffy.sqlite3"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()
        self.dialogue_history = []

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

    def save_raw_output(self, raw_output: str):
        import re
        matches = re.findall(r"(User|Fuffy|Assistant):\s*(.*?)(?=\n(?:User|Fuffy|Assistant):|$)", raw_output, re.DOTALL)

        for role, message in matches:
            role_key = "fuffy" if role.lower() in ["fuffy", "assistant"] else "user"
            message = message.strip()
            if (role_key, message) not in self.dialogue_history:
                self.dialogue_history.append((role_key, message))

    def get_last_context(self, limit=10):
        cursor = self.conn.execute(
            "SELECT role, content FROM memory ORDER BY id DESC LIMIT ?", (limit,)
        )
        messages = reversed(cursor.fetchall())
        return "\n".join([f"{role.capitalize()}: {text}" for role, text in messages])