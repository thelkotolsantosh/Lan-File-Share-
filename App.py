"""
LAN File Share Server
A simple file sharing application to share files between devices on the same WiFi network
"""

import os
import socket
from flask import Flask, render_template_string, request, send_file, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'shared_files'
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500 MB
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mp3', 'zip', 'rar', 'doc', 'docx', 'xls', 'xlsx', 'pptx', 'csv', 'exe', 'apk'}

# Create upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LAN File Share</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            max-width: 600px;
            width: 100%;
            padding: 40px;
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .header h1 {
            color: #333;
            font-size: 28px;
            margin-bottom: 10px;
        }
        
        .header p {
            color: #666;
            font-size: 14px;
        }
        
        .info-box {
            background: #f0f4ff;
            border-left: 4px solid #667eea;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 30px;
        }
        
        .info-box strong {
            color: #333;
        }
        
        .info-box p {
            color: #666;
            font-size: 14px;
            margin: 5px 0;
        }
        
        .upload-section {
            margin-bottom: 40px;
        }
        
        .upload-section h2 {
            color: #333;
            font-size: 18px;
            margin-bottom: 15px;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }
        
        .file-input-wrapper {
            position: relative;
            overflow: hidden;
            display: inline-block;
            width: 100%;
        }
        
        .file-input-wrapper input[type=file] {
            position: absolute;
            left: -9999px;
        }
        
        .upload-label {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 40px;
            border: 2px dashed #667eea;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            background: #f9f9f9;
        }
        
        .upload-label:hover {
            background: #f0f4ff;
            border-color: #764ba2;
        }
        
        .upload-label svg {
            width: 50px;
            height: 50px;
            margin-bottom: 10px;
            color: #667eea;
        }
        
        .upload-label span {
            color: #667eea;
            font-weight: bold;
            font-size: 16px;
            margin-bottom: 5px;
        }
        
        .upload-label p {
            color: #999;
            font-size: 12px;
        }
        
        .upload-btn {
            background: #667eea;
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            width: 100%;
            margin-top: 15px;
            transition: background 0.3s ease;
            font-weight: bold;
        }
        
        .upload-btn:hover {
            background: #764ba2;
        }
        
        .upload-btn:disabled {
            background: #ccc;
            cursor: not-allowed;
        }
        
        .files-section h2 {
            color: #333;
            font-size: 18px;
            margin-bottom: 15px;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }
        
        .files-list {
            list-style: none;
        }
        
        .file-item {
            background: #f9f9f9;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.3s ease;
            border-left: 4px solid #667eea;
        }
        
        .file-item:hover {
            background: #f0f4ff;
            transform: translateX(5px);
        }
        
        .file-info {
            flex: 1;
        }
        
        .file-name {
            color: #333;
            font-weight: bold;
            margin-bottom: 5px;
            word-break: break-word;
        }
        
        .file-meta {
            color: #999;
            font-size: 12px;
        }
        
        .file-actions {
            display: flex;
            gap: 10px;
            margin-left: 10px;
        }
        
        .btn-download {
            background: #667eea;
            color: white;
            padding: 8px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            font-size: 12px;
            transition: background 0.3s ease;
        }
        
        .btn-download:hover {
            background: #764ba2;
        }
        
        .btn-delete {
            background: #ff6b6b;
            color: white;
            padding: 8px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 12px;
            transition: background 0.3s ease;
        }
        
        .btn-delete:hover {
            background: #ee5a52;
        }
        
        .empty-message {
            text-align: center;
            color: #999;
            padding: 30px;
            font-size: 14px;
        }
        
        .error {
            background: #ffe0e0;
            border-left: 4px solid #ff6b6b;
            color: #c92a2a;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        
        .success {
            background: #e0ffe0;
            border-left: 4px solid #51cf66;
            color: #2b8a3e;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        
        .file-count {
            color: #666;
            font-size: 12px;
            margin-top: 10px;
        }
        
        @media (max-width: 600px) {
            .container {
                padding: 20px;
            }
            
            .header h1 {
                font-size: 24px;
            }
            
            .file-item {
                flex-direction: column;
                align-items: flex-start;
            }
            
            .file-actions {
                margin-left: 0;
                margin-top: 10px;
                width: 100%;
            }
            
            .btn-download, .btn-delete {
                flex: 1;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📁 LAN File Share</h1>
            <p>Share files between devices on your WiFi network</p>
        </div>
        
        <div class="info-box">
            <strong>📌 How to connect:</strong>
            <p>Open your browser and go to: <strong>http://{{ local_ip }}:5000</strong></p>
            <p>From any device on the same WiFi network</p>
        </div>
        
        {% if error %}
            <div class="error">❌ {{ error }}</div>
        {% endif %}
        
        {% if success %}
            <div class="success">✅ {{ success }}</div>
        {% endif %}
        
        <div class="upload-section">
            <h2>📤 Upload File</h2>
            <form method="POST" enctype="multipart/form-data">
                <div class="file-input-wrapper">
                    <label for="file" class="upload-label">
                        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path>
                        </svg>
                        <span>Choose file to upload</span>
                        <p>or drag and drop</p>
                    </label>
                    <input type="file" id="file" name="file" required>
                </div>
                <button type="submit" class="upload-btn">🚀 Upload File</button>
            </form>
        </div>
        
        <div class="files-section">
            <h2>📂 Shared Files</h2>
            {% if files %}
                <ul class="files-list">
                    {% for file in files %}
                        <li class="file-item">
                            <div class="file-info">
                                <div class="file-name">📄 {{ file.name }}</div>
                                <div class="file-meta">
                                    Size: {{ file.size }} | Uploaded: {{ file.date }}
                                </div>
                            </div>
                            <div class="file-actions">
                                <a href="/download/{{ file.filename }}" class="btn-download">⬇️ Download</a>
                                <form method="POST" action="/delete/{{ file.filename }}" style="margin: 0;">
                                    <button type="submit" class="btn-delete" onclick="return confirm('Delete this file?')">🗑️ Delete</button>
                                </form>
                            </div>
                        </li>
                    {% endfor %}
                </ul>
                <div class="file-count">Total files: {{ files|length }}</div>
            {% else %}
                <div class="empty-message">
                    📭 No files shared yet. Upload a file to get started!
                </div>
            {% endif %}
        </div>
    </div>
    
    <script>
        // Drag and drop functionality
        const fileInput = document.getElementById('file');
        const uploadLabel = document.querySelector('.upload-label');
        
        uploadLabel.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadLabel.style.background = '#f0f4ff';
            uploadLabel.style.borderColor = '#764ba2';
        });
        
        uploadLabel.addEventListener('dragleave', () => {
            uploadLabel.style.background = '#f9f9f9';
            uploadLabel.style.borderColor = '#667eea';
        });
        
        uploadLabel.addEventListener('drop', (e) => {
            e.preventDefault();
            fileInput.files = e.dataTransfer.files;
            uploadLabel.style.background = '#f9f9f9';
            uploadLabel.style.borderColor = '#667eea';
        });
    </script>
</body>
</html>
"""


def get_local_ip():
    """Get the local IP address of the machine"""
    try:
        # Connect to a non-routable address to determine the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_file_size(size_bytes):
    """Convert bytes to human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def get_files_list():
    """Get list of uploaded files with metadata"""
    files = []
    if os.path.exists(UPLOAD_FOLDER):
        for filename in os.listdir(UPLOAD_FOLDER):
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            if os.path.isfile(filepath):
                size = os.path.getsize(filepath)
                mod_time = os.path.getmtime(filepath)
                mod_date = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M')
                
                files.append({
                    'name': filename,
                    'filename': filename,
                    'size': get_file_size(size),
                    'date': mod_date
                })
        
        # Sort by modification time (newest first)
        files.sort(key=lambda x: os.path.getmtime(os.path.join(UPLOAD_FOLDER, x['filename'])), reverse=True)
    
    return files


@app.route('/')
def index():
    """Main page - display upload form and file list"""
    local_ip = get_local_ip()
    files = get_files_list()
    
    return render_template_string(
        HTML_TEMPLATE,
        local_ip=local_ip,
        files=files,
        error=request.args.get('error'),
        success=request.args.get('success')
    )


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload"""
    # Check if file is present in request
    if 'file' not in request.files:
        return redirect(url_for('index', error='No file selected'))
    
    file = request.files['file']
    
    # Check if file is empty
    if file.filename == '':
        return redirect(url_for('index', error='No file selected'))
    
    # Check file size
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)
    
    if file_size > MAX_FILE_SIZE:
        return redirect(url_for('index', error=f'File too large! Max size: {get_file_size(MAX_FILE_SIZE)}'))
    
    # Validate file type
    if not allowed_file(file.filename):
        return redirect(url_for('index', error='File type not allowed'))
    
    # Save file
    filename = secure_filename(file.filename)
    
    # Handle duplicate filenames
    base, ext = os.path.splitext(filename)
    counter = 1
    original_filename = filename
    while os.path.exists(os.path.join(UPLOAD_FOLDER, filename)):
        filename = f"{base}_{counter}{ext}"
        counter += 1
    
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    
    return redirect(url_for('index', success=f'File uploaded successfully: {filename}'))


@app.route('/download/<filename>')
def download_file(filename):
    """Handle file download"""
    filename = secure_filename(filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    
    # Check if file exists and is safe
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        return redirect(url_for('index', error='File not found'))
    
    try:
        return send_file(filepath, as_attachment=True)
    except Exception as e:
        return redirect(url_for('index', error=f'Error downloading file: {str(e)}'))


@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    """Handle file deletion"""
    filename = secure_filename(filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    
    # Check if file exists and is safe
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        return redirect(url_for('index', error='File not found'))
    
    try:
        os.remove(filepath)
        return redirect(url_for('index', success=f'File deleted: {filename}'))
    except Exception as e:
        return redirect(url_for('index', error=f'Error deleting file: {str(e)}'))


@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file too large error"""
    return redirect(url_for('index', error=f'File too large! Max size: {get_file_size(MAX_FILE_SIZE)}'))


if __name__ == '__main__':
    local_ip = get_local_ip()
    print("\n" + "="*60)
    print("🎉 LAN FILE SHARE SERVER STARTED")
    print("="*60)
    print(f"📍 Local IP: {local_ip}")
    print(f"🌐 Open your browser and go to: http://{local_ip}:5000")
    print(f"💡 Tip: Access from any device on the same WiFi network")
    print("="*60 + "\n")
    
    # Run Flask app
    app.run(
        host='0.0.0.0',  # Listen on all network interfaces
        port=5000,
        debug=True,
        use_reloader=True
    )
