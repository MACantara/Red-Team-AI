#!/usr/bin/env python3
"""
Red Team vs Blue Team AI Simulation - Demo Launcher
==================================================

This script provides an easy way to launch different versions of the cybersecurity simulation.
"""

import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

class SimulationLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Cybersecurity Simulation Launcher")
        self.root.geometry("600x400")
        self.root.configure(bg='#1e1e1e')
        
        self.setup_gui()
        
    def setup_gui(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="🛡️ CYBERSECURITY SIMULATION SUITE 🔴",
            font=("Arial", 18, "bold"),
            fg='#00ff00',
            bg='#1e1e1e'
        )
        title_label.pack(pady=20)
        
        # Description
        desc_label = tk.Label(
            self.root,
            text="Choose your preferred simulation mode:",
            font=("Arial", 12),
            fg='#ffffff',
            bg='#1e1e1e'
        )
        desc_label.pack(pady=10)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg='#1e1e1e')
        button_frame.pack(expand=True, fill='both', padx=50, pady=20)
        
        # GUI Human vs AI button
        gui_button = tk.Button(
            button_frame,
            text="🎮 GUI Mode\n(Human vs AI)",
            command=self.launch_gui_human,
            bg='#0066cc',
            fg='white',
            font=("Arial", 14, "bold"),
            height=3,
            width=20
        )
        gui_button.pack(pady=10, fill='x')
        
        # Auto GUI AI vs AI button
        auto_gui_button = tk.Button(
            button_frame,
            text="🤖 Auto Battle Mode\n(AI vs AI)",
            command=self.launch_auto_gui,
            bg='#cc6600',
            fg='white',
            font=("Arial", 14, "bold"),
            height=3,
            width=20
        )
        auto_gui_button.pack(pady=10, fill='x')
        
        # Console mode button
        console_button = tk.Button(
            button_frame,
            text="💻 Console Mode\n(Classic Text-based)",
            command=self.launch_console,
            bg='#006600',
            fg='white',
            font=("Arial", 14, "bold"),
            height=3,
            width=20
        )
        console_button.pack(pady=10, fill='x')
        
        # Info frame
        info_frame = tk.Frame(self.root, bg='#2d2d2d')
        info_frame.pack(fill='x', padx=20, pady=10)
        
        info_text = """
🎮 GUI Mode: Interactive interface where you play as Blue Team against AI
🤖 Auto Battle: Watch AI vs AI battles with speed controls and statistics  
💻 Console Mode: Traditional text-based interface for focused gameplay
        """
        
        info_label = tk.Label(
            info_frame,
            text=info_text,
            font=("Arial", 10),
            fg='#cccccc',
            bg='#2d2d2d',
            justify='left'
        )
        info_label.pack(padx=10, pady=10)
        
        # Exit button
        exit_button = tk.Button(
            self.root,
            text="❌ Exit",
            command=self.root.quit,
            bg='#cc0000',
            fg='white',
            font=("Arial", 12, "bold"),
            width=10
        )
        exit_button.pack(pady=10)
        
    def get_python_path(self):
        """Get the correct Python executable path"""
        venv_python = r"E:/Projects/Programming-projects/Work-in-Progress/Red-Team-AI/.venv/Scripts/python.exe"
        if os.path.exists(venv_python):
            return venv_python
        return sys.executable
        
    def launch_gui_human(self):
        """Launch the GUI version with human player"""
        try:
            python_path = self.get_python_path()
            subprocess.Popen([python_path, "gui_game.py"])
            messagebox.showinfo("Launched", "GUI Human vs AI mode launched!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch GUI mode: {e}")
            
    def launch_auto_gui(self):
        """Launch the auto GUI version with AI vs AI"""
        try:
            python_path = self.get_python_path()
            subprocess.Popen([python_path, "auto_gui_game.py"])
            messagebox.showinfo("Launched", "Auto Battle AI vs AI mode launched!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Auto Battle mode: {e}")
            
    def launch_console(self):
        """Launch the console version"""
        try:
            python_path = self.get_python_path()
            # Launch in a new terminal window
            if sys.platform.startswith('win'):
                subprocess.Popen(f'start cmd /k "{python_path} main.py"', shell=True)
            else:
                subprocess.Popen(['gnome-terminal', '--', python_path, 'main.py'])
            messagebox.showinfo("Launched", "Console mode launched in new terminal!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Console mode: {e}")

def main():
    root = tk.Tk()
    app = SimulationLauncher(root)
    root.mainloop()

if __name__ == "__main__":
    main()
