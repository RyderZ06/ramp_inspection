import sqlite3
import os

from libra import *

#DB_PATH = r"Z:\Flight Safety Inspection\Группа наземного инспектирования\zas_database\database.db"

#DB_NAME = 'Employees.db'

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Создаем таблицу staff с автоинкрементным id, если еще не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS staff (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            sex TEXT,
            birthday TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Table 'staff' ensured in database.")

def fetch_staff():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, position, sex, birthday, status FROM staff')
    staff = cursor.fetchall()
    conn.close()
    return staff

# old name = insert_employee()
def insert_staff(name, position, sex, birthday, status):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO staff (name, position, sex, birthday, status)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, position, sex, birthday, status))
    conn.commit()
    conn.close()
    print(f"Inserted staff member {name} into database.")

def delete_staff(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM staff WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    print(f"Deleted staff member with id {id} from database.")

# old name update_employee():
def update_staff(id, name, position, sex, birthday, status):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE staff
        SET name = ?, position = ?, sex = ?, birthday = ?, status = ?
        WHERE id = ?
    ''', (name, position, sex, birthday, status, id))
    conn.commit()
    conn.close()
    print(f"Updated staff member with id {id} in database.")

if __name__ == '__main__':
    print("Working directory:", os.getcwd())
    create_table()
    