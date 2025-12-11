from app.data.db import execute_query

# CREATE
def insert_incident(conn, timestamp, severity, category, status, description):
    """
    Inserts a new cyber incident into the table.
    """
    sql = """
    INSERT INTO cyber_incidents (timestamp, severity, category, status, description)
    VALUES (?, ?, ?, ?, ?);
    """
    params = (timestamp, severity, category, status, description)
    return execute_query(conn, sql, params=params, commit=True)

# READ
def get_all_incidents(conn):
    """
    Retrieves all records from the cyber_incidents table with explicit columns.
    """
    sql = "SELECT incident_id, timestamp, severity, category, status, description FROM cyber_incidents ORDER BY timestamp DESC"
    return execute_query(conn, sql)

def get_incident_by_id(conn, incident_id):
    """
    Retrieves a single incident by its ID.
    """
    sql = "SELECT * FROM cyber_incidents WHERE incident_id = ?;"
    params = (incident_id,)
    return execute_query(conn, sql, params=params, fetch_one=True)

# UPDATE
def update_incident_status(conn, incident_id, new_status):
    """
    Updates the status of a specific cyber incident.
    """
    sql = "UPDATE cyber_incidents SET status = ? WHERE incident_id = ?;"
    params = (new_status, incident_id)
    execute_query(conn, sql, params=params, commit=True)
    
def update_incident_severity(conn, incident_id, new_severity):
    """
    Updates the severity of a specific cyber incident.
    """
    sql = "UPDATE cyber_incidents SET severity = ? WHERE incident_id = ?;"
    params = (new_severity, incident_id)
    execute_query(conn, sql, params=params, commit=True)

# DELETE
def delete_incident(conn, incident_id):
    """
    Deletes a specific cyber incident by ID.
    """
    sql = "DELETE FROM cyber_incidents WHERE incident_id = ?;"
    params = (incident_id,)
    execute_query(conn, sql, params=params, commit=True)

# ANALYTICAL READ
def get_incident_stats_by_severity(conn):
    """
    Returns the count of incidents grouped by severity, ordered by risk level.
    """
    sql = """
    SELECT severity, COUNT(incident_id) as count
    FROM cyber_incidents 
    GROUP BY severity 
    ORDER BY CASE severity
        WHEN 'Critical' THEN 1
        WHEN 'High' THEN 2
        WHEN 'Medium' THEN 3
        WHEN 'Low' THEN 4
    END
    """
    return execute_query(conn, sql)