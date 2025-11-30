import bcrypt
from app.data.users import get_user_by_username, insert_user
from app.data.db import connect_database, DATA_DIR
from pathlib import Path

USER_FILE_PATH = DATA_DIR / "users.txt"

def register_user(conn, username, password, role):
    """
    Hashes the password and registers a new user if the username is not taken.
    """
    if get_user_by_username(conn, username):
        print(f"Registration failed: user '{username}' already exists.")
        return False
    
    #Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    #Insert the user into the database
    insert_user(conn, username, hashed_password, role)
    print(f"User '{username}' registered successfully with role '{role}'.")
    return True

def login_user(conn, username, password):
    """
    Authenticates a user by checking the hashed password.
    """
    user_record = get_user_by_username(conn, username)
    