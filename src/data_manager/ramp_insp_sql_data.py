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