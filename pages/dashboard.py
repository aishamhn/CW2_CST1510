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

#example: display all incidents
incident_data = get_all_incidents(CONN)
if incident_data:
    #ensuring column names match incident data structure
    columns = ["ID", "Timestamp", "Severity", "Category", "Status", "Description"]
    df_incidents = pd.DataFrame(incident_data, columns=columns)

    st.dataframe(df_incidents, use_container_width=True)

    #Example: Displaying analytical query results
    st.subheader("Incident Statistics by Severity")
    stats = get_incident_stats_by_severity(CONN)
    if stats:
        df_stats = pd.DataFrame(stats, columns=["Severity", "Count"])
        st.bar_chaty(df_stats, x="Severity", y="Count")
    
else:
    st.info("No cyber incident data available.")

st.markdown("---")
st.caption(f"Welcome back, {st.session_state['username']}!")