import sqlite3
import os

database_name = "sqlite.db"
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, database_name)

def create_db_and_table():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            fio TEXT NOT NULL,
            course INTEGER
        )
    """)
    cur.execute("INSERT OR IGNORE INTO students (id, fio, course) VALUES (1, 'Иванова А.А.', 2)")
    cur.execute("INSERT OR IGNORE INTO students (id, fio, course) VALUES (2, 'Евстигнеев Ф.А.', 3)")
    cur.execute("INSERT OR IGNORE INTO students (id, fio, course) VALUES (3, 'Сидоров И.А.', 4)")
    cur.execute("INSERT OR IGNORE INTO students (id, fio, course) VALUES (4, 'Лупин С.С.', 1)")
    conn.commit()
    conn.close()

def read():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""Select * from students""")
    rows = cur.fetchall()
    for row in rows:
        print(f"id: {row[0]}, fio: {row[1]}, course: {row[2]}")
    conn.close()
    
create_db_and_table()
read()