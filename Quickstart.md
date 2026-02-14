# 🚀 Quick Start Guide

Get LAN File Share running in 5 minutes!

## Step 1: Install Python

### Windows
1. Go to https://www.python.org/downloads/
2. Download Python 3.10 or higher
3. Run the installer
4. ✅ **IMPORTANT**: Check "Add Python to PATH"
5. Click Install

### macOS
```bash
# Install using Homebrew (recommended)
brew install python3

# Or download from https://www.python.org
```

### Linux
```bash
# Ubuntu/Debian
sudo apt-get install python3 python3-pip

# Fedora/RedHat
sudo dnf install python3 python3-pip
```

## Step 2: Download the Project

### Option A: Clone with Git
```bash
git clone https://github.com/yourusername/lan-file-share.git
cd lan-file-share
```

### Option B: Download ZIP
1. Click green "Code" button on GitHub
2. Select "Download ZIP"
3. Extract the folder
4. Open command prompt in that folder

## Step 3: Run the Application

### Windows
1. Double-click `start.bat`
2. A window will open
3. Look for: `http://192.168.X.X:5000`
4. Done! ✅

### macOS/Linux
```bash
chmod +x start.sh      # Make it executable
./start.sh             # Run it
```

You'll see:
```
========================================
LAN FILE SHARE - Startup Script
========================================
Starting LAN File Share Server...
```

## Step 4: Access in Your Browser

Copy the IP address from the terminal output (e.g., `http://192.168.1.100:5000`)

Paste it into any browser on your WiFi network!

## Step 5: Share Files!

Now you can:
- 📤 Upload files
- ⬇️ Download files
- 🗑️ Delete files
- 🔄 Share with other devices

---

## 🆘 Common Problems

### "Python not found" (Windows)
- Did you check "Add Python to PATH" during installation?
- Try: `python --version` in Command Prompt
- If it says "not recognized", reinstall Python and check the PATH option

### "Permission denied" (macOS/Linux)
```bash
chmod +x start.sh
```

### Can't access from other devices
1. Make sure both devices are on **same WiFi**
2. Check the firewall isn't blocking
3. Use the correct IP address
4. Try this command to find your IP:
   - Windows: `ipconfig`
   - Mac/Linux: `ifconfig`

### Port 5000 already in use
A program is using port 5000. Either:
- Close that program
- Or use a different port (edit `app.py` line 283, change `5000` to `5001`)

---

## 📚 Next Steps

- Read the full [README.md](README.md)
- Check [CONTRIBUTING.md](CONTRIBUTING.md) to help improve the project
- Report bugs in GitHub Issues

---

**Stuck? No worries!**
- Read the troubleshooting in README.md
- Check the comments in app.py
- Search GitHub Issues

Happy sharing! 🎉
