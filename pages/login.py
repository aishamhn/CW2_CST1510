import streamlit as st
from app.services.user_service import login_user
from app.data.db import connect_database 

# Re-initialize the connection (ensures connection is available in this page script)
CONN = connect_database() 

st.header("User Login")

if st.session_state.get('logged_in', False):
    st.success(f"You are already logged in as {st.session_state['username']}.")
    st.page_link("pages/dashboard.py", label="Go to Dashboard", icon="📊")
else:
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        submitted = st.form_submit_button("Log In", use_container_width=True)
        
        if submitted:
            role = login_user(CONN, username, password)
            
            if role:
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.session_state['role'] = role
                st.success(f"Login successful! Redirecting to Dashboard...")
              
                st.switch_page("pages/dashboard.py") 
            else:
                st.error("Invalid username or password.")