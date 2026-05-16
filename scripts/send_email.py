import smtplib
import sys
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(data):
    # Hide details by reading directly from Environment Variables
    smtp_user = os.environ.get('SMTP_USER')
    smtp_pass = os.environ.get('SMTP_PASS')
    notify_email = os.environ.get('NOTIFY_EMAIL')

    if not all([smtp_user, smtp_pass, notify_email]):
        print("Error: Missing SMTP environment variables.")
        sys.exit(1)

    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = notify_email
        msg['Subject'] = f"Automation Alert: {data.get('task_name')} - {data.get('status')}"
        
        body = f"""
Hello,

The automation task '{data.get('task_name')}' has completed.

Status: {data.get('status')}
Duration: {data.get('duration')}s
Machine: {data.get('machine_name')}

Logs:
{data.get('stdout') or 'No logs generated'}

Errors:
{data.get('stderr') or 'No errors'}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
        server.quit()
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            log_data = json.loads(sys.argv[1])
            send_email(log_data)
        except Exception as e:
            print(f"Error parsing JSON: {e}")
    else:
        print("Usage: python send_email.py <json_data>")
