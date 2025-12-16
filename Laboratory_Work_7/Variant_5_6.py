import psycopg2
from psycopg2 import sql

def create_tables():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost")
    conn.autocommit = True
    cur = conn.cursor()
    try:
        cur.execute(sql.SQL("CREATE DATABASE {} TEMPLATE template0").format(sql.Identifier("zadanie_6")))
    except Exception as e:
        print(e)
    cur.close()
    conn.close()

    conn2 = psycopg2.connect(dbname="zadanie_6", user="postgres", password="admin", host="localhost")
    cur2 = conn2.cursor()
    cur2.execute("""
        CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    cur2.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            fio TEXT NOT NULL,
            course INTEGER,
            group_id INTEGER REFERENCES groups(id)
        )
    """)
    cur2.execute("INSERT INTO groups (id, name) VALUES (1, '220042') ON CONFLICT DO NOTHING")
    cur2.execute("INSERT INTO groups (id, name) VALUES (2, '220032-11') ON CONFLICT DO NOTHING")
    cur2.execute("INSERT INTO groups (id, name) VALUES (3, '222211') ON CONFLICT DO NOTHING")
    cur2.execute("INSERT INTO groups (id, name) VALUES (4, '220051') ON CONFLICT DO NOTHING")
    cur2.execute("INSERT INTO students (id, fio, course, group_id) VALUES (1, 'Иванова А.А.', 2, 1) ON CONFLICT DO NOTHING")
    cur2.execute("INSERT INTO students (id, fio, course, group_id) VALUES (2, 'Евстигнеев Ф.А.', 3, 2) ON CONFLICT DO NOTHING")
    cur2.execute("INSERT INTO students (id, fio, course, group_id) VALUES (3, 'Сидоров И.А.', 4, 3) ON CONFLICT DO NOTHING")
    cur2.execute("INSERT INTO students (id, fio, course, group_id) VALUES (4, 'Лупин С.С.', 1, 4) ON CONFLICT DO NOTHING")
    conn2.commit()
    cur2.close()
    conn2.close()

def read():
    conn = psycopg2.connect(dbname="zadanie_6", user="postgres", password="admin", host="localhost")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    print("Students:")
    for row in cur.fetchall():
        print(f"id: {row[0]}, fio: {row[1]}, course: {row[2]}, group_id: {row[3]}")
    cur.execute("SELECT * FROM groups")
    print("Groups:")
    for row in cur.fetchall():
        print(f"id: {row[0]}, name: {row[1]}")
    conn.close()

create_tables()
read()