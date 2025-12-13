import streamlit as st
import pandas as pd
from app.data.db import connect_database
from datetime import datetime

#Cyber imports
from app.data.incidents import (
    get_all_incidents, get_incident_stats_by_severity, insert_incident, update_incident_status, update_incident_severity, delete_incident
)

#IT Imports
from app.data.tickets import get_all_it_tickets, get_ticket_stats_by_priority, get_critical_open_tickets

#Data imports
from app.data.datasets import get_all_datasets_metadata, get_dataset_stats_by_uploader

CONN = connect_database()
SEVERITY_OPTIONS = ["Critical", "High", "Medium", "Low"]
STATUS_OPTIONS = ["Open", "In Progress", "Resolved", "Closed"]
CATEGORY_OPTIONS = ["Malware", "Phishing", "DDoS", "Misconfiguration", "Insider Threat"]

#Utility function
def refresh_data():
    """Reruns the script to refresh the dashboard data after a CRUD operation."""
    st.cache_data.clear() #clear cache for data functions
    st.rerun()

#Security check
if not st.session_state.get('logged_in', False):
    st.error("Access Denied. Please log in to view the dashboard")
    st.page_link("pages/login.py", label="Go to Login Page")
    st.stop()

#Dashboard Header
st.header(f"Dashboard")
st.markdown("---")

#using streamlit tabs to organise the three domains
tab_cyber, tab_it, tab_data = st.tabs(["Cyber Incidents", "IT Operations", "Data Metadata"])

#Cyber incidents tab
with tab_cyber:
    st.subheader("Cybersecurity Incident Management")

    #CRUD expander
    with st.expander("Edit Incident Data"):
        crud_tab_c, crud_tab_u, crud_tab_d = st.tabs(["Create", "Update", "Delete"])

        #create (c)
        with crud_tab_c:
            st.markdown("##### New Incident Entry")
            with st.form("create_incident_form"):
                col1, col2 = st.columns(2)
                timestamp = col1.text_input("Timestamp (YYYY-MM-DD HH:MM:SS)", value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                severity = col2.selectbox("Severity", SEVERITY_OPTIONS, index=SEVERITY_OPTIONS.index("High"))
                category = col1.selectbox("Category", CATEGORY_OPTIONS)
                status = col2.selectbox("Status", STATUS_OPTIONS, index=0)
                description = st.text_area("Description")

                if st.form_submit_button("Create new Incident"):
                    if timestamp and severity and description:
                        insert_incident(CONN, timestamp, severity, category, status, description)
                        st.success(f"Incident created successfully (Severity: {severity})")
                        refresh_data()
                    else:
                        st.error("Please fill in all required fields.")
                    
        #Update (u)
        with crud_tab_u:
            st.markdown("##### Update Existing Incident")
            with st.form("update_incident_form"):
                update_id = st.number_input("Incident ID to Update", min_value=1, step=1)
                new_status = st.selectbox("New Status", STATUS_OPTIONS)
                new_severity = st.selectbox("New Severity", SEVERITY_OPTIONS)

                if st.form_submit_button("Update Incident Status and Severity"):
                    if update_id:
                        update_incident_status(CONN, update_id, new_status)
                        update_incident_severity(CONN, update_id, new_severity)
                        st.success(f"Incident ID {update_id} updated to Status: '{new_status}' and Severity: '{new_severity}'")
                        refresh_data()
        
        #Delete (d)
        with crud_tab_d:
            st.markdown("##### Delete Incident")
            with st.form("delete_incident_form"):
                delete_id = st.number_input("Incident ID to Delete", min_value=1, step=1, key="delete_id")

                if st.form_submit_button("Delete Incident", type="primary"):
                    if delete_id:
                        delete_incident(CONN, delete_id)
                        st.success(f"Incident ID {delete_id} deleted.")
                        refresh_data()
        
    #Fetch Data
    incident_data = get_all_incidents(CONN)
    incident_stats = get_incident_stats_by_severity(CONN)

    if incident_data:
        #severity chart
        st.markdown("#### Incident Severity Breakdown")
        df_stats = pd.DataFrame(incident_stats, columns=["Severity", "Count"])
        st.bar_chart(df_stats, x="Severity", y="Count")

        #analysing and giving recommendation
        critical_count = df_stats[df_stats['Severity'] == 'Critical']['Count'].sum()
        if critical_count > 0:
            st.warning(f"**CRITICAL RECOMMENDATION:** There are **{critical_count}** critical incidents detected. Immediate action and resource allocation are required to mitigate risk.")
        else:
            st.success("No critical incidents currently reported")

        st.markdown("#### Raw Incident Data")
        #Full Data Table
        columns = ["ID", "Timestamp", "Severity", "Category", "Status", "Description"]
        df_incidents = pd.DataFrame(incident_data, columns=columns)
        st.dataframe(df_incidents, use_container_width=True)
    else:
        st.info("No cyber incident data available.")

#IT Operations Tab
with tab_it:
    st.subheader("IT Service Mnagement (ITSM) Overview")

    #Fetch Data
    ticket_data = get_all_it_tickets(CONN)
    ticket_stats = get_ticket_stats_by_priority(CONN)
    critical_open_tickets = get_critical_open_tickets(CONN)

    if ticket_data:
        #priority chart
        st.markdown("#### Ticket Priority Distribution")
        df_stats = pd.DataFrame(ticket_stats, columns=["Priority", "Count"])
        st.bar_chart(df_stats, x="Priority", y="Count")

        #analyse and recommend
        if critical_open_tickets:
            count = len(critical_open_tickets)
            st.error(f"**CRITICAL RECOMMENDATION:** **{count}** critical tickets are currently **Open**. Review SLAs immediately and reassign high-priority resources.")
        else:
            st.success("All critical tickets are resolved or in progress.")
        
        st.markdown("#### Critical Open Tickets")
        if critical_open_tickets:
            df_critical = pd.DataFrame(critical_open_tickets, columns=["ID", "Priority", "Description", "Assigned To"])
            st.dataframe(df_critical, use_container_width=True)
        else:
            st.info("No critical open tickets found.")

        st.markdown("#### Raw Ticket Data")
        #Full data table
        columns = ["ID", "Priority", "Description", "Status", "Assigned To", "Created At"]
        df_tickets = pd.DataFrame(ticket_data, columns=columns)
        st.dataframe(df_tickets, use_container_width=True)
    
    else:
        st.info("No IT ticket data available")


#Data Metadata Tab
with tab_data:
    st.subheader("Data Science Metadata & Governance")

    #Fetch Data
    dataset_data = get_all_datasets_metadata(CONN)
    uploader_stats = get_dataset_stats_by_uploader(CONN)

    if dataset_data:
        #uploader statistics chart
        st.markdown("#### Dataset Contributions by Uploader")
        df_uploader = pd.DataFrame(uploader_stats, columns=["Uploader", "Count"])
        st.bar_chart(df_uploader, x="Uploader", y="Count")

        #analyse and recommend
        df_datasets = pd.DataFrame(dataset_data, columns=["ID", "Name", "Rows", "Columns", "Uploader", "Data"])
        largest_dataset = df_datasets.iloc[df_datasets['Rows'].idxmax()]

        st.info(f"**DATA RECOMMENDATION:** The largest dataset is **'{largest_dataset['Name']}'** ({largest_dataset['Rows']} rows). Ensure adequate storage and compute resources are allocated for analysis of this resource.")

        st.markdown("#### Raw Dataset Metadata")
        #Full Data Table
        st.dataframe(df_datasets, use_container_width=True)
    
    else:
        st.info("No dataset metadata available.")