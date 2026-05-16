import sys
import time

def main():
    print("Starting error-prone task...")
    time.sleep(1)
    
    # Simulate an error
    print("Error: Database connection failed!", file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()
