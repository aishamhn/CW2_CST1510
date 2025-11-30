import sqlite3
import pandas as pd
import bcrypt
from pathlib import Path
from datetime import datetime
import os # Added os for path operations

# --- CONFIGURATION ---
DATA_DIR = Path("DATA")
# Ensure the DATA directory exists
# os.makedirs(DATA_DIR, exist_ok=True) # Using pathlib's version:
DATA_DIR.mkdir(exist_ok=True)
# Define the path to your database file
DB_PATH = DATA_DIR / "intelligence_platform.db"

def connect_database(db_path=DB_PATH):
    """
    Establishes a connection to the SQLite database.
    """
    return sqlite3.connect(str(db_path))

def execute_query(conn, query, params=None, fetch_one=False, commit=False):
    """
    Utility function to execute a query, fetch results, and handle connection.
    """
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if commit:
            conn.commit()
            # Return the ID of the last inserted row for CREATE operations
            return cursor.lastrowid

        if fetch_one:
            return cursor.fetchone()
        else:
            return cursor.fetchall()
            
    except sqlite3.Error as e:
        print(f"Database Error executing query: {query}. Error: {e}")
        return None