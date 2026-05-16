-- Database Schema for Execution Logs
-- Compatible with PostgreSQL and SQLite

CREATE TABLE IF NOT EXISTS execution_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Use SERIAL for PostgreSQL
    task_id TEXT NOT NULL,
    task_name TEXT,
    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_time TIMESTAMP,
    status TEXT CHECK(status IN ('SUCCESS', 'FAILED')),
    stdout TEXT,
    stderr TEXT,
    duration FLOAT, -- In seconds
    machine_name TEXT
);

-- Index for faster lookups
CREATE INDEX IF NOT EXISTS idx_task_id ON execution_logs(task_id);
CREATE INDEX IF NOT EXISTS idx_status ON execution_logs(status);
