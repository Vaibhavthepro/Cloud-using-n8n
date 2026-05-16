from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlite3
import os

app = FastAPI(title="Automation Command Center")
templates = Jinja2Templates(directory="dashboard")

# Path to the database
DB_PATH = "/app/data/database.sqlite"

def get_logs():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM execution_logs ORDER BY end_time DESC LIMIT 50")
        logs = cursor.fetchall()
        conn.close()
        return logs
    except:
        return []

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    logs = get_logs()
    
    # Calculate stats
    total = len(logs)
    success = sum(1 for log in logs if log['status'] == 'SUCCESS')
    failed = total - success
    
    # Correct context passing for TemplateResponse
    context = {
        "request": request, 
        "logs": logs,
        "total": total,
        "success": success,
        "failed": failed
    }
    
    return templates.TemplateResponse(request=request, name="index.html", context=context)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
