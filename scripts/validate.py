import pandas as pd
import sqlite3
import os

DB_PATH = "database/jobs.db"

def validate_data():
    print("\n🔍 Running Data Validation...\n")

    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM jobs", conn)

    # Ensure reports folder exists
    os.makedirs("reports", exist_ok=True)

    # -------------------------------
    # 1. Missing Values (Detailed)
    # -------------------------------
    missing = df.isnull().sum()
    missing_df = missing.reset_index()
    missing_df.columns = ["Column", "Missing_Count"]
    missing_df.to_csv("reports/missing_values.csv", index=False)

    # -------------------------------
    # 2. Summary Checks
    # -------------------------------
    duplicate_jobIds = df.duplicated(subset='jobId').sum()

    salary_issues = len(df[df['minimumSalary'] > df['maximumSalary']])

    experience_issues = len(df[df['minimumExperience'] > df['maximumExperience']])

    rating_issues = len(df[(df['AggregateRating'] < 0) | (df['AggregateRating'] > 5)])

    summary_data = [
        ["Duplicate Job IDs", duplicate_jobIds],
        ["Salary Issues", salary_issues],
        ["Experience Issues", experience_issues],
        ["Rating Issues", rating_issues]
    ]

    summary_df = pd.DataFrame(summary_data, columns=["Check", "Value"])
    summary_df.to_csv("reports/validation_summary.csv", index=False)

    print("✅ Validation reports saved:")
    print("   → reports/missing_values.csv")
    print("   → reports/validation_summary.csv")

    # -------------------------------
    # 3. Data Cleaning
    # -------------------------------
    df_cleaned = df.copy()

    # Remove duplicates
    df_cleaned = df_cleaned.drop_duplicates(subset='jobId')

    # Remove invalid salary rows
    df_cleaned = df_cleaned[df_cleaned['minimumSalary'] <= df_cleaned['maximumSalary']]

    # Remove invalid experience rows
    df_cleaned = df_cleaned[df_cleaned['minimumExperience'] <= df_cleaned['maximumExperience']]

    # Optional: Fill missing ratings with median
    if 'AggregateRating' in df_cleaned.columns:
        df_cleaned['AggregateRating'] = df_cleaned['AggregateRating'].fillna(df_cleaned['AggregateRating'].median())

    # Save cleaned data
    df_cleaned.to_sql("jobs_cleaned", conn, if_exists="replace", index=False)

    conn.close()

    print("✅ Cleaned data saved in database (jobs_cleaned)\n")

    return df_cleaned


if __name__ == "__main__":
    validate_data()