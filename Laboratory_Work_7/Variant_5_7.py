import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "sqlite1.db")

def create_tables():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            fio TEXT NOT NULL,
            course INTEGER,
            group_id INTEGER,
            FOREIGN KEY(group_id) REFERENCES groups(id)
        )
    """)
    cur.execute("INSERT OR IGNORE INTO groups (id, name) VALUES (1, '220042')")
    cur.execute("INSERT OR IGNORE INTO groups (id, name) VALUES (2, '220032-11')")
    cur.execute("INSERT OR IGNORE INTO groups (id, name) VALUES (3, '222211')")
    cur.execute("INSERT OR IGNORE INTO groups (id, name) VALUES (4, '220051')")
    cur.execute("INSERT OR IGNORE INTO students (id, fio, course, group_id) VALUES (1, 'Иванова А.А.', 2, 1)")
    cur.execute("INSERT OR IGNORE INTO students (id, fio, course, group_id) VALUES (2, 'Евстигнеев Ф.А.', 3, 2)")
    cur.execute("INSERT OR IGNORE INTO students (id, fio, course, group_id) VALUES (3, 'Сидоров И.А.', 4, 3)")
    cur.execute("INSERT OR IGNORE INTO students (id, fio, course, group_id) VALUES (4, 'Лупин С.С.', 1, 4)")
    conn.commit()
    conn.close()

def read():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM students""")
    rows = cur.fetchall()
    print("Students:")
    for row in rows:
        print(f"id: {row[0]}, fio: {row[1]}, course: {row[2]}, group_id: {row[3]}")
    cur.execute("""SELECT * FROM groups""")
    print("Groups:")
    for row in cur.fetchall():
            print(f"id: {row[0]}, name: {row[1]}")
    conn.close()
    
create_tables()
read()