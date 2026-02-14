#!/bin/bash

# LAN File Share - Linux/macOS Startup Script
# This script activates the virtual environment and runs the Flask server

echo "========================================"
echo "LAN FILE SHARE - Startup Script"
echo "========================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "Please install Python 3 from https://www.python.org"
    exit 1
fi

# Check if venv exists, if not create it
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo ""

# Check if requirements are installed
if ! pip show flask > /dev/null 2>&1; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
    echo ""
fi

# Run the application
echo "Starting LAN File Share Server..."
echo ""
python3 app.py
