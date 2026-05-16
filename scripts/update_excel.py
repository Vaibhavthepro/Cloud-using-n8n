import pandas as pd
import sys
import os
from datetime import datetime

def move_task_to_report(task_id):
    source_file = "/home/node/excel-flow/data/tasks.xlsx"
    report_file = "/home/node/excel-flow/data/tasks_completed_report.xlsx"
    
    try:
        # 1. Read the original file
        df_source = pd.read_excel(source_file)
        
        # 2. Find the task
        clean_id = str(task_id).strip().upper()
        df_source['_match'] = df_source['Task ID'].astype(str).str.strip().str.upper()
        
        # Get the row that finished
        completed_row = df_source[df_source['_match'] == clean_id].copy()
        
        if not completed_row.empty:
            # 3. Update status and time for the report
            completed_row['Status'] = 'Completed'
            completed_row['Completion Time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            completed_row.drop(columns=['_match'], inplace=True)
            
            # 4. Save to the Report File (Append if exists)
            if os.path.exists(report_file):
                df_report = pd.read_excel(report_file)
                df_report = pd.concat([df_report, completed_row], ignore_index=True)
            else:
                df_report = completed_row
                
            df_report.to_excel(report_file, index=False)
            print(f"Task {task_id} moved to report file.")
            
            # 5. REMOVE from original source file
            df_source = df_source[df_source['_match'] != clean_id]
            df_source.drop(columns=['_match'], inplace=True)
            df_source.to_excel(source_file, index=False)
            print("Task removed from original tasks.xlsx.")
        else:
            print(f"Task {task_id} not found in source.")
            
    except Exception as e:
        print(f"Error moving task: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        move_task_to_report(sys.argv[1])
    else:
        print("No Task ID provided.")
        sys.exit(1)
