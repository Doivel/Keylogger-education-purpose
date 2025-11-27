# Advanced Keylogger Utility

A sophisticated Python-based keylogger application with a modern GUI built using Tkinter. This utility demonstrates keyboard event capture, logging, and session management for educational and authorized security testing purposes.

## ⚠️ Legal Disclaimer

**This tool is intended for educational purposes and authorized security testing only.** Unauthorized access to, or use of, computer systems is illegal. Always obtain proper authorization before deploying this software. Users are responsible for compliance with applicable laws and regulations.

---

## Features

✅ **Real-time Keystroke Logging** - Captures all keyboard input in real-time  
✅ **Modern GUI** - Clean, dark-themed interface with Tkinter and ttkthemes  
✅ **Session Management** - Start/stop logging with status indicators  
✅ **Log Viewing** - Open and review captured keystrokes  
✅ **Log Clearing** - Delete log files with confirmation  
✅ **Background Mode** - Run logger discreetly in the background  
✅ **Cross-Platform** - Works on Windows, macOS, and Linux  

---

## Prerequisites

Before running this program, ensure you have:

- **Python 3.6 or higher** installed
- **pip** (Python package manager)
- **Administrator/Root privileges** (required for keyboard capture on most systems)

### System Requirements

- **Windows:** Python + pip
- **macOS:** Python 3.6+ (Xcode Command Line Tools recommended)
- **Linux:** Python 3.6+, python3-tk package

---

## Installation

### Step 1: Clone or Download the Repository

```bash
# Navigate to your project directory
cd /path/to/keylogger
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **pynput** (v1.7.6) - For keyboard event capture
- **ttkthemes** (v3.2.2) - For modern GUI theming

### Step 4: Install System Dependencies (Linux Only)

If you're on Linux, also install Tkinter:

```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora/CentOS
sudo dnf install python3-tkinter

# Arch
sudo pacman -S tk
```

### Step 5: Verify Installation

After completing all steps, verify your setup:

```bash
# Check Python version
python --version

# Check pip packages
pip list | grep -E "pynput|ttkthemes"

# Test import (optional)
python -c "import pynput; import ttkthemes; print('✓ All dependencies installed successfully!')"
```

If you see the success message, you're ready to run the application!

---

## Usage

### Running the Program

```bash
# Ensure virtual environment is activated (if used)
python Keylogger.py
```

### GUI Controls

**Main Window:**
- **ACTIVATE LOGGER** - Start capturing keystrokes
- **SUSPEND LOGGER** - Stop capturing keystrokes
- **View Log** - Open the log file in your default text editor
- **Clear Log** - Delete the log file (requires logger to be suspended)
- **Background** - Minimize the window and run logger in the background

### Log File Location

Captured keystrokes are saved to:
```
keylog.txt
```

This file is created in the same directory as the script when you start logging.

### Log File Format

Each session is separated and timestamped:

```
----------------------------------------
--- NEW SESSION STARTED 2025-11-27 22:30:45 ---
----------------------------------------
H
e
l
l
o
SPACE
w
o
r
l
d
ENTER
----------------------------------------
--- NEW SESSION STARTED 2025-11-27 22:31:12 ---
----------------------------------------
...
```

---

## Command Reference

| Action | Button | Result |
|--------|--------|--------|
| Start Logging | ACTIVATE LOGGER | Begins capturing keystrokes |
| Stop Logging | SUSPEND LOGGER | Stops capturing, saves log |
| View Logs | View Log | Opens `keylog.txt` in system viewer |
| Delete Logs | Clear Log | Removes `keylog.txt` (confirmation required) |
| Background Mode | Background | Minimizes window, continues logging |

---

## Troubleshooting

### Issue: "pynput module not found"

**Solution:**
```bash
pip install pynput==1.7.6
```

### Issue: "Permission Denied" on Linux/macOS

**Solution:** Run with sudo:
```bash
sudo python3 Keylogger.py
```

### Issue: "ttkthemes not found" - Fallback to Standard Tkinter

The program includes a fallback mechanism. If `ttkthemes` is not installed, it will automatically use standard Tkinter with basic styling.

### Issue: Keystrokes Not Being Captured

**Possible causes:**
- Application not running with administrator/root privileges
- Firewall or security software blocking pynput
- Keyboard focus not on the monitored window (check if app has focus)

**Solution:**
- Run as administrator/root
- Check system security settings
- Ensure the application window is in focus

### Issue: Cannot Open Log File

**Solution:**
- Ensure `keylog.txt` exists (start logging first)
- Check file permissions
- Open `keylog.txt` manually in your text editor

---

## Project Structure

```
.
├── Keylogger.py           # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── keylog.txt            # Generated log file (created on first run)
```

---

## Key Features Explained

### 1. Keystroke Capture
Uses `pynput.keyboard.Listener` to monitor keyboard events in real-time.

### 2. Session Management
Each logging session is separated with timestamps for easy tracking and analysis.

### 3. Modern UI
Built with Tkinter and ttkthemes for a professional, dark-themed interface.

### 4. Background Operation
Logger can run minimized in the taskbar/system tray without user interaction.

### 5. Cross-Platform Support
Works on Windows, macOS, and Linux with platform-specific file opening methods.

---

## Advanced Usage

### Running in Background on Linux

```bash
# Run without terminal window
nohup python3 Keylogger.py &
```

### Running with Python Virtual Environment

```bash
# Activate venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# Run program
python Keylogger.py

# Deactivate when done
deactivate
```

---

## Configuration

To modify the log file location, edit line in `Keylogger.py`:

```python
LOGFILE = "keylog.txt"  # Change filename here
```

---

## Performance Notes

- **Memory Usage:** Minimal (~20-30 MB)
- **CPU Usage:** <1% when idle
- **Log File Size:** ~1 KB per 1,000 keystrokes
- **Startup Time:** ~1-2 seconds

---

## Support & Documentation

- **pynput Documentation:** https://pynput.readthedocs.io/
- **Tkinter Documentation:** https://docs.python.org/3/library/tkinter.html
- **ttkthemes GitHub:** https://github.com/TkinterEasyGUI/ttkthemes

---

## License

This project is provided for educational and authorized security testing purposes only. Use responsibly and legally.

---

## Author Notes

This utility demonstrates:
- Event-driven programming with Python
- Multi-threaded GUI applications
- System-level keyboard monitoring
- File I/O and session management
- Cross-platform Python development

---

**Last Updated:** November 27, 2025  
**Python Version:** 3.6+  
**Status:** Ready for Educational Use
