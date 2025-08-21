# config_db.py

import mysql.connector

def create_database():
    conn = mysql.connector.connect('rock.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE complaints(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT NOT NULL,complaint TEXT NOT NULL,status TEXT DEFAULT 'Pending')''')
    conn.commit()
    conn.close()
