import streamlit as st
from app.data.db import connect_database
from app.services.user_service import migrate_users_from_file
from app.data.schema import create_all_tables
from app.services.data_service import load_csv_to_table

#1. Connects to DB and ensures tables/data are ready
@st.cache_resource
def initialize_datatbase():
    """ Connects to DB and performs initial setup only once."""
    conn = connect_database()
    create_all_tables(conn)

    #run migration before loading data (so users are present)
    migrate_users_from_file(conn)

    #load all csv data on startup
    load_csv_to_table(conn, "cyber_incidents.csv", "cyber_incidents")
    load_csv_to_table(conn, "datasets_metadata.csv", "datasets_metadata")
    load_csv_to_table(conn, "it_tickets.csv", "it_tickets")

    return conn

#Global connection object
CONN = initialize_datatbase()

#initialize session state variables if they don't exist
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = None
if 'role' not in st.session_state:
    st.session_state['role'] = None

#Main app entry point
st.set_page_config(
    page_title="Intelligence Platform",
    page_icon="🌐",
    layout="wide"
)

st.title("Multi-Domain Intelligence Platform")
st.markdown("Use the sidebar for navigation.")

if st.session_state['logged_in']:
    st.sidebar.success(f"Logged in as: **{st.session_state['username']}** ({st.session_state['role']})")
    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.session_state['username'] = None
        st.session_state['role'] = None
        st.info("You have been logged out. Please log in again to access the dashboard.")
        #streamlit automatically handles navigation to the default page on state change

else:
    st.sidebar.warning("Please log in or register to continue.")
