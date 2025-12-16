import sqlite3
import os
from functools import lru_cache

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "sqlite1.db")

@lru_cache(maxsize=16)
def get_fio_by_id(id):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT fio FROM students WHERE id = ?", (id,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None

@lru_cache(maxsize=16)
def get_fio_by_course(course):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT fio FROM students WHERE course = ?", (course,))
    rows = cur.fetchall()
    conn.close()
    return [row[0] for row in rows]

print(get_fio_by_id(1))
print(get_fio_by_id(2))
print(get_fio_by_course(1))
print(get_fio_by_course(3))