from app.data.db import execute_query

def insert_user(conn, username, hashed_password, role):
    """
    Inserts a new user into the 'users' table.
    """
    sql = "INSERT INTO users (username, hashed_password, role) VALUES (?, ?, ?)"
    # Note: hashed_password is stored as a string, must decode from bytes if needed
    params = (username, hashed_password.decode('utf-8'), role)
    return execute_query(conn, sql, params=params, commit=True)

def get_user_by_username(conn, username):
    """
    Retrieves a user record by username.
    """
    sql = "SELECT username, hashed_password, role FROM users WHERE username = ?"
    params = (username,)
    return execute_query(conn, sql, params=params, fetch_one=True)