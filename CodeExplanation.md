# 📚 Code Explanation - LAN File Share

A beginner-friendly guide explaining how the LAN File Share application works.

## Table of Contents
1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [How It Works](#how-it-works)
4. [Main Code Walkthrough](#main-code-walkthrough)
5. [Common Tasks Explained](#common-tasks-explained)

---

## Overview

LAN File Share is a **web application** built with Flask that allows sharing files between devices on the same WiFi network.

### Key Concepts

**Flask**: A Python library for building web applications
- Creates a web server you can access from a browser
- Handles incoming requests (file uploads, downloads, etc.)
- Serves HTML (the web page) to your browser

**HTML/CSS**: Used to display the web interface
- HTML = Content and structure
- CSS = Styling and appearance

**Python**: The programming language
- Handles logic (uploading, downloading, deleting files)
- Manages file storage on disk

---

## Project Structure

```
lan-file-share/
│
├── app.py                    ← Main Flask application
├── config.py                 ← Configuration settings
├── requirements.txt          ← Dependencies
├── test_app.py              ← Unit tests
│
├── Documentation
├── README.md                 ← Main documentation
├── QUICKSTART.md            ← Quick start guide
├── CODE_EXPLANATION.md      ← This file
├── CONTRIBUTING.md          ← Contribution guidelines
├── CHANGELOG.md             ← Version history
│
├── Deployment
├── Dockerfile               ← Docker configuration
├── docker-compose.yml       ← Docker Compose
│
├── Configuration
├── .env.example             ← Example environment variables
├── .gitignore              ← Git ignore rules
├── .dockerignore           ← Docker ignore rules
│
├── Startup Scripts
├── start.bat               ← Windows startup
├── start.sh                ← Linux/macOS startup
│
└── shared_files/           ← Uploaded files go here
```

---

## How It Works

### 1. Starting the Server

When you run `python app.py`:

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

- Creates a Flask web server
- Listens on port 5000
- Accessible from any device on your network

### 2. Request Flow

```
Browser Request
      ↓
Flask Route Handler
      ↓
Python Function (e.g., upload_file)
      ↓
Save/Load File
      ↓
Response to Browser
```

### 3. File Storage

Files are stored in the `shared_files/` folder:
- Created automatically when app starts
- Files persist even after you close the app
- Can be accessed from the file system

---

## Main Code Walkthrough

### Part 1: Imports and Setup

```python
from flask import Flask, render_template_string, request, send_file
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
```

**What's happening:**
- `Flask`: Creates the web application
- `render_template_string`: Sends HTML to the browser
- `request`: Accesses data sent from the browser (files, form data)
- `send_file`: Sends files to download
- `secure_filename`: Prevents security issues with filenames

### Part 2: Configuration

```python
UPLOAD_FOLDER = 'shared_files'
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500 MB
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', ...}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
```

**What's happening:**
- Sets where files are saved
- Sets maximum file size
- Lists allowed file types
- Creates the folder if it doesn't exist

### Part 3: Helper Functions

```python
def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
```

**What's happening:**
- Checks if a file type is safe to upload
- Splits filename at the last dot: `photo.jpg` → `['photo', 'jpg']`
- Returns `True` if extension is in ALLOWED_EXTENSIONS, `False` otherwise

```python
def get_file_size(size_bytes):
    """Convert bytes to human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
```

**What's happening:**
- Converts `1048576` bytes to `1.0 MB`
- Loops through units (B → KB → MB → GB)
- Returns formatted string

### Part 4: Flask Routes

A **route** is a URL path that triggers a Python function.

#### Home Page Route

```python
@app.route('/')
def index():
    """Main page - display upload form and file list"""
    local_ip = get_local_ip()
    files = get_files_list()
    
    return render_template_string(HTML_TEMPLATE, ...)
```

**What happens:**
- `@app.route('/')` - When user visits `http://192.168.1.100:5000/`
- Gets your local IP address
- Gets list of files in `shared_files/`
- Sends HTML template to browser with this data

#### Upload Route

```python
@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload"""
    if 'file' not in request.files:
        return redirect(url_for('index', error='No file selected'))
    
    file = request.files['file']
    # ... validation ...
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    
    return redirect(url_for('index', success='File uploaded!'))
```

**Step by step:**
1. Check if user sent a file
2. Get the file object from the request
3. Validate file size and type
4. Make filename safe (remove dangerous characters)
5. Create full path: `shared_files/myfile.txt`
6. Save the file to disk
7. Redirect back to home page with success message

#### Download Route

```python
@app.route('/download/<filename>')
def download_file(filename):
    """Handle file download"""
    filename = secure_filename(filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    
    if not os.path.exists(filepath):
        return redirect(url_for('index', error='File not found'))
    
    return send_file(filepath, as_attachment=True)
```

**What happens:**
1. User clicks download button with filename
2. Check if file exists and is safe
3. Send file to browser
4. Browser downloads it

#### Delete Route

```python
@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    """Handle file deletion"""
    filename = secure_filename(filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    
    if not os.path.exists(filepath):
        return redirect(url_for('index', error='File not found'))
    
    os.remove(filepath)
    return redirect(url_for('index', success='File deleted!'))
```

**What happens:**
1. User clicks delete button with filename
2. Check if file exists
3. Delete the file from disk
4. Redirect back with success message

---

## Common Tasks Explained

### Task 1: Add a New File Type

**Goal**: Allow `.mp4` video files

**Steps:**
1. Open `app.py`
2. Find line 17: `ALLOWED_EXTENSIONS = {...}`
3. Add `'mp4'` to the set:
   ```python
   ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', ..., 'mp4'}
   ```

### Task 2: Change Maximum File Size

**Goal**: Allow 1 GB files instead of 500 MB

**Steps:**
1. Open `app.py`
2. Find line 16: `MAX_FILE_SIZE = 500 * 1024 * 1024`
3. Change to:
   ```python
   MAX_FILE_SIZE = 1000 * 1024 * 1024  # 1 GB
   ```

### Task 3: Change the Port Number

**Goal**: Use port 8000 instead of 5000

**Steps:**
1. Open `app.py`
2. Go to the bottom: `app.run(...)`
3. Change `port=5000` to `port=8000`
4. Now access at `http://192.168.1.100:8000`

### Task 4: Add a New Route

**Goal**: Add an "About" page

**Steps:**
```python
@app.route('/about')
def about():
    """About page"""
    return render_template_string("""
        <h1>About LAN File Share</h1>
        <p>Version 1.0.0</p>
    """)
```

Now visit `http://192.168.1.100:5000/about`

---

## Understanding Key Python Concepts

### 1. Decorators (`@app.route()`)

```python
@app.route('/')
def index():
    pass
```

**What it means:**
- `@` symbol indicates a decorator
- Adds behavior to the function below
- `@app.route('/')` means: "When user visits `/`, run this function"

### 2. F-strings

```python
filepath = os.path.join(UPLOAD_FOLDER, filename)
print(f"File saved to {filepath}")
```

**What it means:**
- `f"..."` is an f-string (formatted string)
- `{variable}` inserts the variable's value
- Result: `"File saved to shared_files/myfile.txt"`

### 3. List Comprehensions

```python
files = [f for f in os.listdir(UPLOAD_FOLDER) if os.path.isfile(...)]
```

**What it means:**
- `[... for ... in ...]` creates a list
- Equivalent to:
```python
files = []
for f in os.listdir(UPLOAD_FOLDER):
    if os.path.isfile(...):
        files.append(f)
```

### 4. Dictionary Operations

```python
file_info = {
    'name': 'document.pdf',
    'size': '2.5 MB',
    'date': '2024-01-15'
}

print(file_info['name'])  # Access: document.pdf
```

**What it means:**
- `{}` creates a dictionary (key-value pairs)
- `file_info['name']` accesses the value for key 'name'

---

## Data Flow Example

**Uploading a File:**

1. **Browser**: User selects file and clicks upload
2. **HTML Form**: Sends file to `POST /upload`
3. **Flask**: Route handler catches the request
4. **Python**: 
   - Validates the file
   - Creates safe filename
   - Saves to `shared_files/`
5. **Database**: File now stored on disk
6. **Response**: Redirect to home page
7. **Browser**: Shows success message
8. **Display**: New file appears in the file list

---

## Debugging Tips

### 1. Check Console Output

```
Running on http://192.168.1.100:5000
```

The terminal shows:
- Server status
- Errors
- Debug information

### 2. Read Error Messages

```
FileNotFoundError: [Errno 2] No such file or directory: 'shared_files'
```

**Translation**: The folder doesn't exist yet

**Fix**: Run the code, it will create it

### 3. Use Print Statements

```python
def upload_file():
    print("Upload request received")  # ← Add this
    print(f"File: {file.filename}")   # ← And this
    # ... rest of code
```

Check the console for output

### 4. Use Browser DevTools

Press `F12` in your browser:
- **Console** tab: JavaScript errors
- **Network** tab: Request/response data
- **Elements** tab: HTML structure

---

## Learning Resources

- **Python Basics**: https://python.org/tutorial
- **Flask Docs**: https://flask.palletsprojects.com
- **HTTP/Web Basics**: https://developer.mozilla.org/en-US/docs/Web/HTTP
- **File I/O**: https://docs.python.org/3/tutorial/inputoutput.html

---

## Next Steps

1. **Run the app** and explore the web interface
2. **Read the code** and comments in `app.py`
3. **Make small changes** (e.g., add a file type)
4. **Try the exercises** below

---

## Exercises for Learning

### Exercise 1: Add a Timestamp to Filenames
**Goal**: Save files with current date/time

**Hint**: Use `datetime.now()`

```python
from datetime import datetime
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
```

### Exercise 2: Limit File Count
**Goal**: Only allow 10 files maximum

**Hint**: Check `len(files)` before saving

```python
if len(files) >= 10:
    return redirect(url_for('index', error='Maximum 10 files!'))
```

### Exercise 3: Add a Search Feature
**Goal**: Search files by name

**Hint**: Filter the files list

```python
search_term = request.args.get('search', '')
filtered_files = [f for f in files if search_term.lower() in f.lower()]
```

---

**Happy Learning! 🚀**

Feel free to modify the code, break things, and learn from the results!
