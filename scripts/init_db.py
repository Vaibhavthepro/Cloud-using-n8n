import sqlite3
import os

def init_db():
    db_path = os.path.join("data", "database.sqlite")
    schema_path = os.path.join("docs", "schema.sql")
    
    if not os.path.exists("data"):
        os.makedirs("data")
        
    if not os.path.exists(schema_path):
        print(f"Error: {schema_path} not found!")
        return

    print(f"Initializing database at: {db_path}...")
    
    try:
        conn = sqlite3.connect(db_path)
        with open(schema_path, 'r') as f:
            schema = f.read()
            conn.executescript(schema)
        conn.commit()
        conn.close()
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Failed to initialize database: {e}")

if __name__ == "__main__":
    init_db()
