import streamlit as st
from app.services.user_service import register_user
from app.data.db import connect_database 

CONN = connect_database()

st.header("New User Registration")

if st.session_state.get('logged_in', False):
    st.warning("You must log out before registering a new user.")
    
else:
    with st.form("register_form"):
        new_username = st.text_input("Choose Username")
        new_password = st.text_input("Choose Password", type="password")
        new_role = st.selectbox("Select Role", ["analyst", "cyber_admin", "data_analyst", "admin"])
        
        submitted = st.form_submit_button("Register", use_container_width=True)
        
        if submitted:
            if new_username and new_password:
                success = register_user(CONN, new_username, new_password, new_role)
                if success:
                    st.success(f"User {new_username} registered successfully! You can now log in.")
                    st.page_link("pages/login.py", label="Go to Login Page")
            else:
                st.warning("Please fill in all fields.")