import sqlite3 as sq
import os

from libra import *

#DB_NAME = 'Employees.db'

def create_table():
    with sq.connect (DB_PATH) as con:
        cur = con.cursor()

        cur.execute('''
        CREATE TABLE IF NOT EXISTS staff (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            gender TEXT,
            birthday TEXT,
            status TEXT
        )
    ''')
    print("Table 'staff' ensured in database.")

def fetch_staff():
    conn = sq.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, position, gender, birthday, status FROM staff')
    staff = cursor.fetchall()
    conn.close()
    return staff

def insert_staff(name, position, gender, birthday, status):
    conn = sq.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO staff (name, position, gender, birthday, status)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, position, gender, birthday, status))
    conn.commit()
    conn.close()
    print(f"Inserted staff member {name} into database.")

def delete_staff(id):
    conn = sq.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM staff WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    print(f"Deleted staff member with id {id} from database.")

def update_staff(id, name, position, gender, birthday, status):
    conn = sq.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE staff
        SET name = ?, position = ?, gender = ?, birthday = ?, status = ?
        WHERE id = ?
    ''', (name, position, gender, birthday, status, id))
    conn.commit()
    conn.close()
    print(f"Updated staff member with id {id} in database.")

if __name__ == '__main__':
    print("Working directory:", os.getcwd())
    create_table()
    