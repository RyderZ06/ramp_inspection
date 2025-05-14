import sqlite3 as sq
import os

from libra import *

def create_ramp_table():
    with sq.connect (DB_PATH) as con:
        cur = con.cursor()

        cur.execute('''
        CREATE TABLE IF NOT EXISTS ramp_inspection (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reg_number	TEXT NOT NULL,
        	open_date DATE NOT NULL,
        	finding_status TEXT NOT NULL,
        	close_date DATE NOT NULL,
        	aircraft_type TEXT NOT NULL,
        	finding TEXT,
        	category TEXT,
        	reference TEXT,
        	action_taken TEXT,
        	audit_number TEXT NOT NULL,
        	audit_type TEXT NOT NULL,
        	auditor_name TEXT NOT NULL,
        	location INTEGER NOT NULL,
        	finding_number INTEGER,
        	item TEXT,
        	customer TEXT NOT NULL,
        	department TEXT,
        	recommended_corrective_action TEXT,
        	country TEXT NOT NULL,
        )
    ''')
    print("Table 'ramp_inspection' ensured in database.")

def fetch_ramp():
    with sq.connect (DB_PATH) as con:
        cur = con.cursor()
        cur.execute('SELECT id, reg_number, open_date, finding_status, close_date, aircraft_type, finding, category, reference, action_taken, audit_number, audit_type, auditor_name, location, finding_number, item, customer, department, recommended_corrective_action, country FROM ramp_inspection')
        ramp_inspection = cur.fetchall()
        return ramp_inspection

def insert_ramp(
    reg_number, open_date, finding_status, close_date,
    aircraft_type, finding, category, reference, action_taken,
    audit_number, audit_type, auditor_name, location, finding_number,
    item, customer, department, recommended_corrective_action, country
):
    with sq.connect (DB_PATH) as con:
        cur = con.cursor()
        cur.execute('''
            INSERT INTO ramp_inspection (
            reg_number, open_date, finding_status, close_date,
            aircraft_type, finding, category, reference, action_taken,
            audit_number, audit_type, auditor_name, location, finding_number,
            item, customer, department, recommended_corrective_action, country)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (reg_number, open_date, finding_status, close_date,
              aircraft_type, finding, category, reference, action_taken,
              audit_number, audit_type, auditor_name, location, finding_number,
              item, customer, department, recommended_corrective_action, country))
        con.commit()
        print(f"Inserted ramp_inspection member {name} into database.")

def delete_ramp(id):
    with sq.connect (DB_PATH) as con:
        cur = con.cursor()
        cur.execute('DELETE FROM ramp_inspection WHERE id = ?', (id,))
        con.commit()
        print(f"Deleted staff member with id {id} from database.")

def update_ramp(id, reg_number, open_date, finding_status, close_date,
                aircraft_type, finding, category, reference, action_taken,
                audit_number, audit_type, auditor_name, location, finding_number,
                item, customer, department, recommended_corrective_action, country):
    with sq.connect (DB_PATH) as con:
        cur = con.cursor()
        cur.execute('''
            UPDATE ramp_inspection
            SET reg_number = ?, open_date = ?, finding_status = ?, close_date = ?,
            aircraft_type = ?, finding = ?, category = ?, reference = ?,
            action_taken = ?,audit_number = ?, audit_type = ?, auditor_name = ?,
            location = ?, finding_number = ?, item = ?, customer = ?, department = ?,
            recommended_corrective_action = ?, country = ?
            WHERE id = ?
        ''', (reg_number, open_date, finding_status, close_date,
              aircraft_type, finding, category, reference, action_taken,
              audit_number, audit_type, auditor_name, location, finding_number,
              item, customer, department, recommended_corrective_action, country, id))
        con.commit()
        print(f"Updated ramp_inspection member with id {id} in database.")

if __name__ == '__main__':
    print("Working directory:", os.getcwd())
    create_table()
         