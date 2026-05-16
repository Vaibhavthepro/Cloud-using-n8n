# Portable Deployment Guide (Pendrive)

This project is designed to be portable, allowing you to run the automation system from a USB pendrive on any Windows machine.

## 1. Portable Python
Instead of installing Python on the host machine, use a portable version:
- Download **WinPython** or the **Python Embeddable Package**.
- Extract it to a folder named `python_portable` in the project root.
- Update your n8n "Execute Command" nodes to use:
  `./python_portable/python.exe {{script_path}}`

## 2. Portable n8n
- Use the **n8n Desktop App** which is relatively self-contained.
- Alternatively, if you have Node.js portable, run n8n using:
  `npx n8n start`

## 3. SQLite for Portability
- Use **SQLite** instead of PostgreSQL. 
- The database file `data/database.sqlite` will travel with your pendrive.
- In n8n, use the **SQLite Node** and point it to:
  `{{$env.PROJECT_ROOT}}/data/database.sqlite`

## 4. Relative Paths
Ensure all paths in your Excel file and n8n environment variables are relative to the pendrive's drive letter. 
> [!TIP]
> Since drive letters change (e.g., D:, E:, F:), use a startup script to detect the current drive and set the `PROJECT_ROOT` environment variable dynamically.

### Example `start_portable.bat`:
```batch
@echo off
set PROJECT_ROOT=%~dp0
echo Project Root set to: %PROJECT_ROOT%
npx n8n start
```

## 5. Summary
- **Storage**: All scripts, data, and logs stay on the pendrive.
- **Independence**: No need to install software on the host computer.
- **Security**: Take your automation system with you!
