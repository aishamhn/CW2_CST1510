import sqlite3
import pandas as pd
import bcrypt
from pathlib import Path
from datetime import datetime
import os # added os for path operations

#configuration
DATA_DIR =Path("DATA")
#ensure the DATA directory exists
DATA_DIR.mkdir(exist_ok=True)
#defining the path to the database file
DB_PATH = DATA_DIR / "intelligence_platform.db"

def connect_database(db_path=DB_PATH):
    """
    establishes a connection to the SQLite database.
    """
    return sqlite3.connect(str(db_path))

def execute_query(conn, query, params=None, fetch_one=False, commit=False):
    """
    utility function to execute a query, fetch results, and handle connection.
    """
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        if commit:
            conn.commit()
            #return the ID of the last inserted row for CREATE operations
            return cursor.lastrowid
        
        if fetch_one:
            return cursor.fetchone()
        else:
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error executing query: {query}. Error: {e}")
        return None