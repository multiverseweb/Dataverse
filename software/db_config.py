import os
import sys
import sqlite3

# Define the user data directory in APPDATA to avoid read-only Program Files errors
app_data_dir = os.path.join(os.getenv('APPDATA', os.path.expanduser('~')), 'Dataverse')

# Ensure the directory exists
if not os.path.exists(app_data_dir):
    os.makedirs(app_data_dir)

DB_FILE = os.path.join(app_data_dir, "dataverse.db")

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Locate database.sql depending on if we are running from source or frozen PyInstaller
    if getattr(sys, 'frozen', False):
        # In PyInstaller, data files are in sys._MEIPASS
        # We added it via --add-data "software\database.sql;software"
        sql_file = os.path.join(sys._MEIPASS, "software", "database.sql")
    else:
        sql_file = os.path.join(os.path.dirname(__file__), "database.sql")
        
    if os.path.exists(sql_file):
        with open(sql_file, "r") as f:
            sql_script = f.read()
        try:
            cursor.executescript(sql_script)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
    else:
        print(f"Could not find {sql_file}")
        
    conn.close()

# Initialize tables when db_config is imported
init_db()