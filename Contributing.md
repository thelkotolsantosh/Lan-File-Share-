# Contributing to LAN File Share

Thank you for your interest in contributing to LAN File Share! 🎉

This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive feedback
- Avoid harassment or discrimination

## How to Contribute

### 1. Report Bugs

If you find a bug, please open an issue on GitHub with:
- **Clear title** describing the bug
- **Description** of what's happening
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Screenshots** (if applicable)
- **Your environment** (OS, Python version, etc.)

### 2. Suggest Enhancements

Have an idea to improve the project?
- Open an issue with the label "enhancement"
- Describe the feature and why it would be useful
- Include examples or mockups if relevant

### 3. Submit Code Changes

#### Prerequisites
- Python 3.7+
- Git installed
- GitHub account

#### Step-by-Step Process

1. **Fork the Repository**
   - Click the "Fork" button on GitHub
   - This creates your own copy

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/lan-file-share.git
   cd lan-file-share
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
   
   Branch naming:
   - Features: `feature/descriptive-name`
   - Bug fixes: `bugfix/issue-description`
   - Documentation: `docs/what-you-changed`

4. **Set Up Development Environment**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # Activate it
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

5. **Make Your Changes**
   - Write clean, readable code
   - Add comments for complex logic
   - Follow PEP 8 style guide (see below)
   - Keep changes focused and concise

6. **Test Your Changes**
   ```bash
   # Run the application
   python app.py
   
   # Test in your browser
   # http://localhost:5000
   ```

7. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   Commit message guidelines:
   - Use present tense ("Add feature" not "Added feature")
   - Be descriptive but concise
   - Reference issues: "Fix #123"
   - Example: "Add file search functionality - Fix #45"

8. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

9. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill in the template:
     - Description of changes
     - Why these changes are needed
     - Any related issues
   - Submit!

## Coding Standards

### Python Style Guide (PEP 8)

```python
# ✅ Good
def upload_file(filename):
    """Upload a file to the server."""
    if not filename:
        return None
    
    # Save file logic here
    return True


# ❌ Avoid
def uploadFile(filename):
    if not filename: return None
    # save file
    return True
```

### Best Practices

1. **Use meaningful names**
   ```python
   # ✅ Good
   uploaded_files = os.listdir(UPLOAD_FOLDER)
   
   # ❌ Avoid
   files = os.listdir(x)
   ```

2. **Add docstrings**
   ```python
   def get_file_size(size_bytes):
       """Convert bytes to human-readable format."""
       # Implementation
   ```

3. **Keep functions small**
   - One function = one responsibility
   - Easier to test and understand

4. **Comment complex logic**
   ```python
   # Handle duplicate filenames by adding counter
   counter = 1
   while os.path.exists(filepath):
       counter += 1
   ```

5. **Use type hints** (Python 3.7+)
   ```python
   def get_files_list() -> list:
       """Get list of uploaded files."""
   ```

## File Structure

Keep the project organized:

```
lan-file-share/
├── app.py                    # Main application
├── requirements.txt          # Dependencies
├── setup.py                  # Package setup
├── README.md                 # Documentation
├── CONTRIBUTING.md           # This file
├── LICENSE                   # MIT License
├── .gitignore               # Git ignore rules
├── .env.example             # Example environment config
└── shared_files/            # Uploaded files folder
```

## Documentation

- Update **README.md** if you add/change features
- Add docstrings to new functions
- Comment non-obvious code
- Update this CONTRIBUTING.md if needed

## Pull Request Review Process

When you submit a PR:

1. Maintainers will review your code
2. They may suggest changes
3. Update your PR if needed
4. Once approved, it will be merged!

### PR Review Checklist

Your PR should have:
- ✅ Clear description of changes
- ✅ Tests (if applicable)
- ✅ Updated documentation
- ✅ No conflicts with main branch
- ✅ Follows coding standards

## Common Issues

### "Permission denied" when pushing
```bash
# Check your Git credentials
git config user.name
git config user.email

# Or use SSH instead of HTTPS
git remote set-url origin git@github.com:YOUR_USERNAME/lan-file-share.git
```

### "Merge conflicts"
```bash
# Update your branch with latest code
git fetch origin
git merge origin/main

# Resolve conflicts in your editor
# Then commit and push
git add .
git commit -m "Resolve merge conflicts"
git push origin your-branch
```

## Questions?

- Ask in GitHub issues
- Check existing discussions
- Review the README for setup help

## Recognition

Contributors are acknowledged in:
- The project README
- GitHub contributors page
- Release notes (for major contributions)

Thank you for making LAN File Share better! 🚀
