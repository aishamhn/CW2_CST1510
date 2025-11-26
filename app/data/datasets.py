from app.data.db import execute_query

def get_all_datasets_metadata(conn):
    """
    retrieves all records from the datasets_metadata table.
    """
    sql = "SELECT * FROM datasets_metadata;"
    return execute_query(conn, sql)