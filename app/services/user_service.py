import bcrypt
from app.data.users import get_user_by_username, insert_user
from app.data.db import connect_database, DATA_DIR
from pathlib import Path

USERS_FILE_PATH = DATA_DIR / "users.txt"

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

    if user_record:
        #user_record is (username, hashed_password, role)
        db_username, db_hashed_password, db_role = user_record

        #compare the provided password with the stored hash
        if bcrypt.checkpw(password.encode('utf-8'), db_hashed_password.encode('utf-8')):
            return db_role
        else:
            return None #Invalid password
    else:
        return None #user not found
    
def migrate_users_from_file(conn, filepath=USERS_FILE_PATH):
    """
    Reads users from the old users.txt file and moves them to the database.
    """
    try:
        if not filepath.exists():
            print(f"Migration skipped: user file '{filepath}' not found.")
            return 0
        
        with open(filepath, 'r') as f:
            lines = f.readlines()

        migrated_count = 0
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) == 2:
                username, role = parts[0], parts[1]
                #using a common placeholder password for migrated users
                placeholder_password = "password123"

                #check if user already exists before registering
                if not get_user_by_username(conn, username):
                    register_user(conn, username, placeholder_password, role)
                    migrated_count += 1
        
        print(f"--- User migration complete: {migrated_count} new users migrated/registered. ---\n")
        return migrated_count
    
    except Exception as e:
        print(f"An error occurred during migration: {e}")
        return 0