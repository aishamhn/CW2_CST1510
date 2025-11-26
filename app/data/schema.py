from app.data.db import execute_query

#users table
def create_users_table(conn):
    """Creates the 'users' table for authentication."""
    sql = """
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        hashed_password TEXT NOT NULL,
        role TEXT NOT NULL
    );
    """
    execute_query(conn, sql, commit=True)
    print("Table 'users' created.")

#domain tables
def create_cyber_incidents_table(conn):
    """Creates the 'cyber_incidents' table."""
    sql = """
    CREATE TABLE IF NOT EXISTS cyber_incidents (
        incident_id INTEGER PRIMARY KEY,
        timestamp TEXT,
        severity TEXT,
        category TEXT,
        status TEXT,
        description TEXT
    );
    """
    execute_query(conn, sql, commit=True)
    print("Table 'cyber_incidents' created.")


def create_datasets_metadata_table(conn):
    """Creates the 'datasets_metadata' table."""
    sql = """
    CREATE TABLE IF NOT EXISTS datasets_metadata (
        dataset_id INTEGER PRIMARY KEY,
        name TEXT,
        rows INTEGER,
        columns INTEGER,
        uploaded_by TEXT,
        upload_date TEXT
    );
    """
    execute_query(conn, sql, commit=True)
    print("Table 'datasets_metadata' created.")


def create_it_tickets_table(conn):
    """Creates the 'it_tickets' table."""
    sql = """
    CREATE TABLE IF NOT EXISTS it_tickets (
        ticket_id INTEGER PRIMARY KEY,
        priority TEXT,
        description TEXT,
        status TEXT,
        assigned_to TEXT,
        created_at TEXT,
        resolution_time_hours INTEGER
    );
    """
    execute_query(conn, sql, commit=True)
    print("Table 'it_tickets' created.")


def create_all_tables(conn):
    """Runs all table creation functions."""
    print("\n--- Creating All Tables ---")
    create_users_table(conn)
    create_cyber_incidents_table(conn)
    create_datasets_metadata_table(conn)
    create_it_tickets_table(conn)
    print("---------------------------\n")