@echo off
REM LAN File Share - Windows Startup Script
REM This script activates the virtual environment and runs the Flask server

echo ========================================
echo LAN FILE SHARE - Windows Startup
echo ========================================
echo.

REM Check if venv exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Check if requirements are installed
pip show flask > nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    echo.
)

REM Run the application
echo Starting LAN File Share Server...
echo.
python app.py

pause
