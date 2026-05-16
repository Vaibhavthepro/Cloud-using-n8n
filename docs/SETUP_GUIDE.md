# Setup Guide

Follow these steps to set up the **Cross-Platform Excel-Based Automation and Monitoring System** on your machine.

## Prerequisites
- **Python 3.10+**: [Download here](https://www.python.org/)
- **n8n**: Desktop app or installed via npm (`npm install n8n -g`)
- **Git** (Optional)

## Step 1: Install Python Dependencies
Open your terminal in the project root and run:
```bash
pip install pandas openpyxl
```

## Step 2: Import n8n Workflow
1.  Open **n8n**.
2.  Go to **Workflows** > **Add Workflow** > **Import from File**.
3.  Select `workflow/excel_automation_workflow.json`.
4.  Configure the **Environment Variables** in n8n (see `.env.example` section below).

## Step 3: Initialize Database
- **Option A: SQLite (Recommended for Local/Portable)**:
  1. Open your terminal in the project root.
  2. Run the initialization script:
     ```bash
     python scripts/init_db.py
     ```
  3. This will create `data/database.sqlite` with the correct tables.
- **Option B: PostgreSQL**:
  1. Create a database and run the schema found in `docs/schema.sql`.
  2. Update the credentials in the **PostgreSQL Node** within n8n.

## Step 4: Environment Variables
Create a `.env` file in the project root (or set them in n8n):
```env
PROJECT_ROOT=C:/Users/YourName/Desktop/excel-flow
DASHBOARD_API_URL=https://your-dashboard-api.com

# Email Notifications
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_gmail_app_password
NOTIFY_EMAIL=recipient_email@gmail.com

# Telegram (Optional)
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id
```

> [!IMPORTANT]
> If using Gmail, you MUST use an **App Password**, not your regular password. Enable 2FA and generate one in your Google Account security settings.

## Step 5: Start the Workflow
1.  Toggle the workflow to **Active** in n8n.
2.  The scheduler will now run every 1 minute.
3.  You can manually trigger it by clicking **Execute Workflow** to test immediately.

## Step 6: Testing
1.  Open `data/tasks.xlsx`.
2.  Ensure a task has `Status = Pending` and `Schedule Time` is in the past or current.
3.  Watch the n8n execution log to see the script run.
4.  Check the `execution_logs` table in your database.

---

## Troubleshooting
- **Script Path Error**: Ensure the path in Excel is relative to the project root or absolute.
- **Python Not Found**: Ensure Python is in your system PATH.
- **Excel Locked**: Close the Excel file before n8n runs, as Windows might prevent writing while it's open.
