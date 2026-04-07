import aiosqlite
import json

DB_FILE = "approvals.db"


async def init_db():
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS approvals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input TEXT,
            output TEXT,
            decision TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        await db.commit()


async def save_approval(user_input, result):
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute(
            "INSERT INTO approvals (input, output, decision) VALUES (?, ?, ?)",
            (user_input, json.dumps(result), result["overall_decision"])
        )
        await db.commit()


async def fetch_all():
    async with aiosqlite.connect(DB_FILE) as db:
        cursor = await db.execute("SELECT * FROM approvals")
        rows = await cursor.fetchall()
        return rows
