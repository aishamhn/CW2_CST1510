import streamlit as st
import pandas as pd
from app.data.db import connect_database
from app.data.incidents import get_all_incidents, get_incident_stats_by_severity

CONN = connect_database()

#Security check
if not st.session_state.get('logged_in', False):
    st.error("Access Denied. Please log in to view the dashboard.")
    st.page_link("pages/login.py", label="Go to Login Page")
    st.stop()

#Dashboard Content (only runs if logged in)
st.header(f"Dashboard: {st.session_state['role'].upper()} Access")
st.subheader("Cyber incidents overview")
st.markdown("---")

