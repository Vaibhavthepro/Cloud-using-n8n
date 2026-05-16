import subprocess
import json
import sys

def check_storage():
    print("--- SYSTEM STORAGE CHECK START ---")
    print("Executing command: df -h /")
    
    try:
        # Run the real storage command
        result = subprocess.check_output(['df', '-h', '/']).decode('utf-8')
        
        # Format the output for the terminal
        print("COMMAND OUTPUT:")
        print(result)
        
        # Prepare data for Excel/DB
        data = {
            "status": "success",
            "storage_info": result.split('\n')[1]
        }
        
        print("--- STORAGE CHECK COMPLETE ---")
        return data
    except Exception as e:
        print(f"FAILED to check storage: {e}")
        sys.exit(1)

if __name__ == "__main__":
    check_storage()
