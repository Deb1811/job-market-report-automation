import pandas as pd
import sqlite3

DB_PATH = "database/jobs.db"

def extract_top_skills(df):
    skills_series = df['tagsAndSkills'].dropna()
    skills = skills_series.str.split(',')
    skills = skills.explode()
    skills = skills.str.strip().str.lower()
    skills = skills[skills != ""]
    return skills.value_counts().head(10)

def salary_by_role(df):
    df['avg_salary'] = (df['minimumSalary'] + df['maximumSalary']) / 2
    return df.groupby('title')['avg_salary'].mean().sort_values(ascending=False).head(10)

def jobs_trend(df):
    print("📊 Processing Job Trends...")

    temp = df['jobUploaded'].dropna().astype(str).str.lower()

    def convert_to_days(x):
        try:
            if "day" in x:
                num = x.split()[0]
                return int(num) if num.isdigit() else None

            elif "hour" in x or "just" in x or "today" in x:
                return 0

            elif "+" in x:   # handles "30+ days ago"
                return int(x.split("+")[0])

            else:
                return None

        except:
            return None

    days = temp.apply(convert_to_days)
    days = days.dropna()

    if len(days) == 0:
        print("⚠️ No valid trend data found\n")
        return pd.Series()

    bins = [0, 1, 3, 7, 14, 30, 60]
    labels = ["0-1 days", "1-3 days", "3-7 days", "7-14 days", "14-30 days", "30+ days"]

    trend = pd.cut(days, bins=bins, labels=labels).value_counts().sort_index()

    print("✅ Job Trends processed\n")

    return trend
   

def transform_data():
    print("\n📊 Running Data Transformation...\n")

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM jobs_cleaned", conn)

    df['avg_salary'] = (df['minimumSalary'] + df['maximumSalary']) / 2

    total_jobs = len(df)
    avg_salary = df['avg_salary'].mean()

    top_companies = df['companyName'].value_counts().head(5)
    top_roles = df['title'].value_counts().head(5)
    top_locations = df['location'].value_counts().head(5)

    # NEW
    top_skills = extract_top_skills(df)
    role_salary = salary_by_role(df)
    trend = jobs_trend(df)

    conn.close()

    print("✅ Transformation Complete\n")

    return {
        "total_jobs": total_jobs,
        "avg_salary": avg_salary,
        "top_companies": top_companies,
        "top_roles": top_roles,
        "top_locations": top_locations,
        "top_skills": top_skills,
        "role_salary": role_salary,
        "trend": trend
    }


if __name__ == "__main__":
    transform_data()