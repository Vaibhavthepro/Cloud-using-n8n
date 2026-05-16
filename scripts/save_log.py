import sqlite3
import sys
import os

def save_log(args):
    # Order: task_id, task_name, start_time, end_time, status, stdout, stderr, duration, machine_name
    db_path = "/home/node/excel-flow/data/database.sqlite"
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        query = """
        INSERT INTO execution_logs 
        (task_id, task_name, start_time, end_time, status, stdout, stderr, duration, machine_name)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        cursor.execute(query, args)
        conn.commit()
        conn.close()
        print("Log saved successfully.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) >= 10:
        # sys.argv[0] is script name, 1-9 are our data
        save_log(sys.argv[1:10])
    else:
        print(f"Error: Expected 9 arguments, got {len(sys.argv)-1}")
        sys.exit(1)
