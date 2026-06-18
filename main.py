import sqlite3
from fastapi import FastAPI

app = FastAPI()
connect = sqlite3.connect('example.db', check_same_thread=False)
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY,
        title TEXT,
        completed TEXT
    )
""")

connect.commit()

@app.get("/")
def home():
    return {
        "message": "SQLite connected fine"
    }
