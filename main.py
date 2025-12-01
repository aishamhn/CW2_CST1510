from app.data.db import connect_database, DATA_DIR
from app.data.schema import create_all_tables
from app.services.user_service import register_user, login_user, migrate_users_from_file
from app.services.data_service import load_csv_to_table
from app.data.incidents import (
    insert_incident, get_all_incidents,
    update_incident_status, delete_incident,
    get_incident_by_id, get_incident_stats_by_severity
)
#assuming other CRUD/Read functions exist in other files
from app.data.datasets import get_all_datasets_metadata
from app.data.tickets import get_all_it_tickets
from pathlib import Path
import getpass #For securely reading the password

def setup_database(conn):
    """
    Sets up the entire database: create tables, registers core users, and loads CSV data.
    """
    print("--- Database Setup Started ---")

    #1. Create all tables
    create_all_tables(conn)

    #2. Prepare users.txt for migration (if it doesn't exist)
    placeholder_users_path = DATA_DIR / "users.txt"
    if not placeholder_users_path.exists():
        with open(placeholder_users_path, 'w') as f:
            f.write("admin,cyber_admin\n")
            f.write("analyst,data_analyst\n")
    
    #3. Migrate/Register Users
    migrate_users_from_file(conn)

    #4 Load CSV Data
    print("\n--- Loading Domain Data ---")
    load_csv_to_table(conn, "cyber_incidents.csv", "cyber_incidents")
    load_csv_to_table(conn, "datasets_metadata.csv", "datasets_metadata")
    load_csv_to_table(conn, "it_tickets.csv", "it_tickets")
    print("---------------------------\n")

    # --- INTERACTIVE USER FUNCTIONS ---

def interactive_register(conn):
    """Prompts user for registration details."""
    print("\n-- Register New User --")
    username = input("Enter desired username: ")
    #use getpass to hide the password input
    password = getpass.getpass("Enter password: ")
    role = input("Enter role (e.g., analyst, admin): ")

    #call the core service function
    register_user(conn, username, password, role)

def interactive_login(conn):
    """Prompts user for login details and attempts authentication."""
    print("\n-- User login--")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    #call the core service function
    role = login_user(conn, username, password)

    if role:
        print(f"Login successful! Welcome, {username} ({role})")
        return role
    else:
        print("Login failed: Invalid username or password.")
        return None


def interactive_menu(conn):
    """Main interactive loop for testing authentication."""
    setup_database(conn)

    current_role = None

    while True:
        print("\n====================================")
        print("         MAIN MENU (SQL LAB)         ")
        print("====================================")
        if current_role:
            print(f"Logged in as: {current_role}")
            print("1. Logout")
            print("2. Test CRUD operations (Demo)")
            print("3. Exit application")
        else:
            print("1. Register New user")
            print("2. Login")
            print("3. Exit Application")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            if current_role:
                current_role = None
                print("Logged out successfully.")
            else:
                interactive_register(conn)
        elif choice == "2":
            if current_role:
                # user is logged in, run demo
                run_comprehensive_tests(conn)
            else:
                current_role = interactive_login(conn)
        elif choice == "3":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def run_comprehensive_tests(conn):
    """
    Runs a test sequence for CRUD operations on cyber_incidents.
    """
    print("\n--- DEMO: CRUD Operations on Cyber Incidents ---")

    # CREATE (Insert)
    incident_id = insert_incident(
        conn, "2025-11-20 09:00:00:000000", "Critical", "Zero-Day Exploit", "Open", "A critical new incident created via the application."
    )
    if incident_id:
        print(f"New incident created with ID: {incident_id}")
    
    #READ ALL
    all_incidents = get_all_incidents(conn)
    print(f"Total Incidents after insert: {len(all_incidents)} records.")

    # READ by ID
    new_incident = get_incident_by_id(conn, incident_id)
    print(f"New Incident data (Status): {new_incident[4]}")

    #UPDATE
    update_incident_status(conn, incident_id, "In Progress")
    updated_incident = get_incident_by_id(conn, incident_id)
    print(f"Incident ID {incident_id} Status updated to: {updated_incident[4]}")

    #ANALYTICAL READ
    stats = get_incident_stats_by_severity(conn)
    print(f"Incidents by Severity (Top 3): {stats[:3]}")

    #DELETE
    delete_incident(conn, incident_id)
    deleted_incident = get_incident_by_id(conn, incident_id)
    print(f"Incident ID {incident_id} after deletion: {deleted_incident}")

    #Other Reads
    datasets = get_all_datasets_metadata(conn)
    print(f"Dataset Metadata loaded: {len(datasets)} records.")
    tickets = get_all_it_tickets(conn)
    print(f"IT Tickets loaded: {len(tickets)} records.")

    print("\n--- DEMO COMPLETE ---")
    

if __name__ == '__main__':
    # 1. connect to the database
    conn = connect_database()

    # 2. Start the interactive menu
    interactive_menu(conn)

    # 3. close the connection
    conn.close() 