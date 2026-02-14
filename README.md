# 📁 LAN File Share

A simple, fast, and beautiful file sharing application for your local network. Share files between any devices connected to the same WiFi network - no configuration needed!

Perfect for:
- 📱 Sharing files between your phone, laptop, and desktop
- 💻 Quick file transfers without cloud storage
- 🏠 Home network file sharing
- 🎓 Classroom file distribution
- 🏢 Office file sharing (LAN)

## ✨ Features

- **🌐 Web-Based Interface** - Access from any device with a browser
- **📤 Easy Upload** - Drag & drop files or click to select
- **⬇️ Quick Download** - Download any shared file instantly
- **🗑️ File Management** - Delete files you no longer need
- **🎨 Beautiful UI** - Modern, responsive design works on phones and computers
- **⚡ Fast Transfer** - Direct LAN transfers (no internet needed)
- **🔒 Secure** - Only accessible on your local network
- **💾 No Setup** - Just run it and start sharing!

## 📋 System Requirements

- **Python 3.7** or higher
- **pip** (comes with Python)
- **WiFi Network** (devices must be on same network)

## 🚀 Installation

### Step 1: Clone or Download the Repository

```bash
git clone https://github.com/yourusername/lan-file-share.git
cd lan-file-share
```

Or download as ZIP and extract.

### Step 2: Create a Virtual Environment (Recommended)

A virtual environment keeps your project dependencies separate from your system Python.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You'll see `(venv)` in your terminal after activation.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs Flask (the web framework we're using).

### Step 4: Run the Application

```bash
python app.py
```

You should see output like:

```
============================================================
🎉 LAN FILE SHARE SERVER STARTED
============================================================
📍 Local IP: 192.168.1.100
🌐 Open your browser and go to: http://192.168.1.100:5000
💡 Tip: Access from any device on the same WiFi network
============================================================
```

## 🌐 How to Use

### Starting the Server

1. Run `python app.py` on your main computer
2. Note the **Local IP** shown (e.g., `192.168.1.100`)

### Accessing from Other Devices

**From any device on the same WiFi:**

1. Open a web browser (Chrome, Safari, Firefox, Edge, etc.)
2. Go to: `http://192.168.1.100:5000` (replace IP with yours)
3. You'll see the file sharing interface

### Uploading Files

**Method 1 - Click to Upload:**
1. Click the "Choose file to upload" button
2. Select a file from your device
3. Click "🚀 Upload File"

**Method 2 - Drag and Drop:**
1. Click and drag a file from your File Explorer/Finder
2. Drop it on the upload area
3. It uploads automatically!

### Downloading Files

1. In the "Shared Files" section, find the file you want
2. Click the "⬇️ Download" button
3. The file downloads to your Downloads folder

### Deleting Files

1. Find the file in the list
2. Click "🗑️ Delete" next to it
3. Confirm deletion
4. File is removed

## 📂 File Structure

```
lan-file-share/
│
├── app.py                   # Main Flask application (the server)
├── requirements.txt         # List of dependencies (Flask, Werkzeug)
├── README.md               # This file (documentation)
├── .gitignore             # Files to ignore in git
├── LICENSE                # MIT License
├── setup.py               # Package setup configuration
│
└── shared_files/           # Folder where uploaded files are stored
    ├── document.pdf
    ├── photo.jpg
    └── video.mp4
```

**What each file does:**

| File | Purpose |
|------|---------|
| `app.py` | The main program - contains all the logic for file sharing |
| `requirements.txt` | Lists what libraries the program needs (Flask, Werkzeug) |
| `README.md` | Instructions and documentation (what you're reading) |
| `.gitignore` | Tells git which files to ignore (venv, shared_files, etc.) |
| `LICENSE` | Legal terms (MIT License - open source) |
| `setup.py` | Allows installing the project as a Python package |

## 🔧 Common Issues & Solutions

### "Address already in use"
Another program is using port 5000. Either:
- Close the other program
- Or modify line 283 in `app.py` from `port=5000` to `port=5001`

### "Connection refused" or can't access the server
Check:
1. Both devices are on the **same WiFi network**
2. Firewall isn't blocking Python (accept when prompted)
3. You're using the correct IP address from the terminal

### "ModuleNotFoundError: No module named 'flask'"
Make sure you:
1. Activated your virtual environment (`source venv/bin/activate`)
2. Ran `pip install -r requirements.txt`

### How do I find my computer's IP?

**Windows:**
```bash
ipconfig
```
Look for "IPv4 Address" (usually starts with 192.168...)

**macOS/Linux:**
```bash
ifconfig
```
Look for "inet" (usually starts with 192.168...)

### Can I access this from the internet?
No - it only works on your local WiFi network. This is a **security feature**. If you want internet access, you'd need a more complex setup with authentication.

## 📚 For Beginners

### What is Flask?
Flask is a Python library that helps you create web applications. It runs a web server so you can access your application through a browser.

### What is a Virtual Environment?
A virtual environment is like a isolated container for your project. It keeps your project's dependencies separate from your computer's system Python. This prevents version conflicts.

### How to activate/deactivate venv

**Activate:**
- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

**Deactivate:**
```bash
deactivate
```

### What's the difference between `python` and `python3`?
- `python3` is for Python version 3.x (recommended)
- `python` might be Python 2 (deprecated)
- On Windows, `python` usually works; on Mac/Linux use `python3`

## 🎨 Customization

### Change the Port Number
In `app.py`, line 283:
```python
app.run(host='0.0.0.0', port=5001)  # Changed from 5000 to 5001
```

### Change Maximum File Size
In `app.py`, line 16:
```python
MAX_FILE_SIZE = 1000 * 1024 * 1024  # 1 GB instead of 500 MB
```

### Allow More File Types
In `app.py`, line 17:
```python
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'mp4', 'exe', 'app'}  # Add/remove extensions
```

## 🚀 Advanced Usage

### Run on Startup (Windows)
Create a batch file `start.bat`:
```batch
@echo off
cd /d "%~dp0"
source venv\Scripts\activate
python app.py
pause
```

Double-click to start.

### Run as Background Service (Linux/macOS)
```bash
nohup python app.py > server.log 2>&1 &
```

## 📈 Future Enhancements

Ideas to extend this project:
- 🔐 Add password protection
- 📊 Show upload/download statistics
- 🏷️ Add file categories/tags
- 🔍 Search functionality
- 👥 Multiple user accounts
- 📱 Mobile app
- 🎥 Real-time file transfer progress

## 🤝 Contributing

Want to improve this project?

1. **Fork** the repository on GitHub
2. **Create a branch**: `git checkout -b feature/your-feature`
3. **Make changes** to the code
4. **Commit**: `git commit -m "Add new feature"`
5. **Push**: `git push origin feature/your-feature`
6. **Open a Pull Request**

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

MIT License means:
- ✅ Free to use
- ✅ Free to modify
- ✅ Free to distribute
- ⚖️ Include the license in your distribution

## 💬 Support

Need help?

1. **Check the Troubleshooting section** above
2. **Read the code comments** - they explain what each part does
3. **Google the error message** - many others have faced the same issue
4. **Check Flask documentation**: https://flask.palletsprojects.com/

## 📚 Learning Resources

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Flask Quick Start](https://flask.palletsprojects.com/quickstart/)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [Git & GitHub Guide](https://guides.github.com/)
- [HTTP & Web Basics](https://developer.mozilla.org/en-US/docs/Web/HTTP)

**Happy file sharing!** 🎉

Made with ❤️ for the Python community
