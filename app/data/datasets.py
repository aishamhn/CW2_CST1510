from app.data.db import execute_query

def get_all_datasets_metadata(conn):
    """
    Retrieves all records from the datasets_metadata table for exploration.
    (Preserving your requested function name)
    """
    # Explicitly selecting columns is best practice
    sql = "SELECT dataset_id, name, rows, columns, uploaded_by, upload_date FROM datasets_metadata ORDER BY upload_date DESC"
    return execute_query(conn, sql, fetch_one=False)

def get_dataset_stats_by_uploader(conn):
    """
    Retrieves dataset counts grouped by uploader for visualization and analysis.
    """
    sql = "SELECT uploaded_by, COUNT(dataset_id) as count FROM datasets_metadata GROUP BY uploaded_by"
    return execute_query(conn, sql, fetch_one=False)