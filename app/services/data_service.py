import pandas as pd
from app.data.db import connect_database
from app.data.db import DB_PATH #Import DB_PATH for utility functions

def load_csv_to_table(conn, csv_filename, table_name):
    """
    Loads data from a CSV file into the specified database table.

    :param conn: The database connection object.
    :param csv_filename: The name of the CSV file in the DATA directory.
    :param table_name: The target table name in the database.
    """
    csv_path = DB_PATH.parent / csv_filename

    try:
        #1. Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(str(csv_path))

        #2. Use the DataFrame's to_sql method to insert into the database
        df.to_sql(
            name=table_name,
            con=conn,
            if_exists='append', #'append' adds new data. 'replace' deletes old data
            index=False # Do not write the DataFrame's index column
        )
        print(f"Successfully loaded {len(df)} rows from '{csv_filename}' into '{table_name}'.")

    except FileNotFoundError:
        print(f"Error: CSV file not found at '{csv_path}'.")
    except Exception as e:
        print(f"Error loading data into {table_name}: {e}")