import schedule
import time
from main import run_pipeline

# Run every Monday at 9 AM
schedule.every().monday.at("09:00").do(run_pipeline)

print("⏳ Scheduler started... Waiting for scheduled time.")

while True:
    schedule.run_pending()
    time.sleep(60)
    