import sys
import time
import json
import socket

def main():
    print("Starting sample task execution...")
    
    # Simulate some work
    time.sleep(2)
    
    # Sample output data
    result = {
        "status": "success",
        "data": {
            "processed_count": 100,
            "machine": socket.gethostname()
        }
    }
    
    print(json.dumps(result))
    print("Task completed successfully.")

if __name__ == "__main__":
    main()
