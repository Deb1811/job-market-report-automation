import smtplib
from email.message import EmailMessage

def send_email():
    msg = EmailMessage()
    msg['Subject'] = 'Automated Job Market Report'
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = 'receiver_email@gmail.com'

    msg.set_content('Attached is your automated job market report.')

    # Attach file
    with open('reports/job_report.xlsx', 'rb') as f:
        msg.add_attachment(
            f.read(),
            maintype='application',
            subtype='xlsx',
            filename='job_report.xlsx'
        )

    # Send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('debakshisaha12sc@gmail.com', 'fusm msfj nvat sdot')
        smtp.send_message(msg)

    print("📧 Email sent successfully!")