from app.data.db import execute_query

def get_all_it_tickets(conn):
    """Retrieves all rows from the it_tickets table."""
    sql = "SELECT ticket_id, priority, description, status, assigned_to, created_at FROM it_tickets ORDER BY created_at DESC"
    return execute_query(conn, sql, fetch_one=False)

def get_ticket_status_by_priority(conn):
    """
    Retrieves ticket counts grouped by priority, ordered by severity.
    """
    sql="""
    SELECT priority, COUNT(ticket_id) as count
    FROM it_tickets
    GROUP BY priority
    ORDER BY CASE priority
        WHEN 'Critical' THEN 1
        WHEN 'High' THEN 2
        WHEN 'Medium' THEN 3
        WHEN 'Low' THEN 4
    END
    """
    return execute_query(conn, sql, fetch_one=False)

def get_critical_open_tickets(conn):
    """Retrieves critical tickets that are currently open."""
    sql = "SELECT ticket_id, priority, description, assigned_to FROM it_tickets WHERE priority = 'Critical' AND status = 'Open'"
    return execute_query(conn, sql, fetch_one=False)