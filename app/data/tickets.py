from app.data.db import execute_query

def get_all_it_tickets(conn):
    """
    Retrieves all records from the it_tickets table.
    """
    sql = "SELECT * FROM it_tickets;"
    return execute_query(conn, sql)