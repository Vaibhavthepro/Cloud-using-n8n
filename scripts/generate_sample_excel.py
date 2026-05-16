import pandas as pd
import os

def create_sample_excel():
    data = [
        {
            "Task ID": "TASK_001",
            "Task Name": "Daily System Check",
            "Script Path": "scripts/sample_task.py",
            "Schedule Time": "09:00",
            "Priority": "High",
            "Status": "Pending",
            "Retry Count": 0,
            "Output Path": "logs/task_001.log"
        },
        {
            "Task ID": "TASK_002",
            "Task Name": "Error Test Task",
            "Script Path": "scripts/error_task.py",
            "Schedule Time": "10:00",
            "Priority": "Medium",
            "Status": "Pending",
            "Retry Count": 0,
            "Output Path": "logs/task_002.log"
        }
    ]
    
    df = pd.DataFrame(data)
    file_path = os.path.join("data", "tasks.xlsx")
    
    # Ensure data directory exists
    if not os.path.exists("data"):
        os.makedirs("data")
        
    df.to_excel(file_path, index=False)
    print(f"Sample Excel file created at: {file_path}")

if __name__ == "__main__":
    create_sample_excel()
