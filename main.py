from scripts.extract import load_data
from scripts.validate import validate_data
from scripts.report import create_report
from scripts.email_sender import send_email

def run_pipeline():
    print("\n🚀 Running Automated Business Report Pipeline...\n")

    load_data()
    validate_data()
    create_report()
    send_email()

    print("\n✅ Pipeline Completed Successfully!\n")


if __name__ == "__main__":
    run_pipeline()