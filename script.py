import pandas as pd
import sqlite3
import os

# Configuration
# Note the 'r' at the start and the filename at the end!
DATA_PATH = r'C:\Users\niakh\Desktop\course material\CV projects\PythonSQLproject\online_retail_II.csv'
DB_NAME = 'retail_db.sqlite'
TABLE_NAME = 'transactions'

# UPDATE THIS BLOCK IN YOUR SCRIPT

# 1. Update the filename to match what you actually downloaded (likely .xlsx)
DATA_PATH = r'C:\Users\niakh\Desktop\course material\CV projects\PythonSQLproject\online_retail_II.xlsx' 

def load_data():
    if not os.path.exists(DATA_PATH):
        print(f"Error: File not found at {DATA_PATH}. Check the filename and extension!")
        return

    print("--- Starting Data Ingestion ---")
    
    print("Reading Excel file... (This might take 1-2 minutes)")
    # CHANGED: read_excel instead of read_csv
    df = pd.read_excel(DATA_PATH, engine='openpyxl') 
    
    print(f"Connecting to database: {DB_NAME}")
    conn = sqlite3.connect(DB_NAME)
    
    print(f"Writing {len(df)} rows to table '{TABLE_NAME}'...")
    df.to_sql(TABLE_NAME, conn, if_exists='replace', index=False)
    
    print("--- Ingestion Complete ---")
    conn.close()

def query_data():
    """
    Demonstrates how to pull data back from SQL for analysis.
    """
    conn = sqlite3.connect(DB_NAME)
    
    # Example SQL Query: Filter out cancelled transactions (usually start with 'C')
    query = """
    SELECT * FROM transactions 
    WHERE Invoice NOT LIKE 'C%' 
    LIMIT 5
    """
    
    print("\nSample Query Output (Clean Transactions):")
    result = pd.read_sql(query, conn)
    print(result)
    
    conn.close()

if __name__ == "__main__":
    load_data()
    query_data()