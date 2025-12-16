import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "sqlite.db")

def delete():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE fio != 'Евстигнеев Ф.А.'")
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
    
delete()
read()
