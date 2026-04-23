import pandas as pd
import sqlite3
import os

DB_PATH = "database/jobs.db"
DATA_PATH = "data/jobs.csv"

def load_data():
    # Load CSV with correct encoding
    df = pd.read_csv(DATA_PATH, encoding='latin1')

    print("✅ Data Loaded Successfully")
    print(df.head())

    # Ensure database folder exists
    os.makedirs("database", exist_ok=True)

    # Connect to SQLite
    conn = sqlite3.connect(DB_PATH)

    # Store raw data
    df.to_sql("jobs", conn, if_exists="replace", index=False)

    conn.close()

    print("✅ Data stored in database (table: jobs)")

    return df


if __name__ == "__main__":
    load_data()