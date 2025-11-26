from app.data.db import execute_query

def get_all_it_tickets(conn):
    """
    retrieves all records from the it_ticket table.
    """
    sql = "SELECT * FROM it_ticket;"
    return execute_query(conn, sql)