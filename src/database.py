import sqlite3
import os

DB_NAME = 'Employees.db'

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            id TEXT PRIMARY KEY,
            employee TEXT,
            role TEXT,
            gender TEXT,
            birthday TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Table 'Employees' ensured in database.")

def fetch_employees():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Employees')
    employees = cursor.fetchall()
    conn.close()
    return employees

def insert_employee(id, employee, role, gender, birthday, status):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO Employees (id, employee, role, gender, birthday, status) VALUES (?, ?, ?, ?, ?, ?)',
                      (id, employee, role, gender, birthday, status))
        conn.commit()
        print(f"Inserted employee {id} into database.")
    except sqlite3.IntegrityError as e:
        print(f"Error inserting employee: {e}")
        raise
    finally:
        conn.close()

def delete_employee(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Employees WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    print(f"Deleted employee {id} from database.")

def update_employee(new_employee, new_role, new_gender, new_birthday, new_status, id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE Employees SET employee = ?, role = ?, gender = ?, birthday = ?, status = ? WHERE id = ?",
                  (new_employee, new_role, new_gender, new_birthday, new_status, id))
    conn.commit()
    conn.close()
    print(f"Updated employee {id} in database.")

def id_exists(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Employees WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

def list_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    print("Tables in database:", tables)

if __name__ == '__main__':
    print("Working directory:", os.getcwd())
    create_table()
    list_tables()
    