import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import time
import random
from environment import Environment
from ai import RedTeamAI


class CyberSecurityGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Red Team vs Blue Team - Cybersecurity Simulation")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1e1e1e')
        
        # Game state
        self.environment = Environment()
        self.red_ai = RedTeamAI(actions=["scan", "exploit", "brute_force", "social_engineering"])
        self.game_running = False
        self.round_count = 0
        self.blue_score = 0
        self.red_score = 0
        self.game_paused = False
        
        # Enhanced stats
        self.total_rounds = 0
        self.blue_wins = 0
        self.red_wins = 0
        self.avg_detection_time = 0
        
        self.setup_gui()
        
    def setup_gui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#1e1e1e')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="🛡️ CYBERSECURITY BATTLE ARENA 🔴",
            font=("Arial", 20, "bold"),
            fg='#00ff00',
            bg='#1e1e1e'
        )
        title_label.pack(pady=(0, 20))
        
        # Top frame for scores and controls
        top_frame = tk.Frame(main_frame, bg='#1e1e1e')
        top_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Score display
        self.setup_score_display(top_frame)
        
        # Game controls
        self.setup_game_controls(top_frame)
        
        # Middle frame for game state
        middle_frame = tk.Frame(main_frame, bg='#1e1e1e')
        middle_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Left panel - System state
        self.setup_system_state(middle_frame)
        
        # Center panel - Action controls
        self.setup_action_controls(middle_frame)
        
        # Right panel - Statistics
        self.setup_statistics_panel(middle_frame)
        
        # Bottom frame for logs
        self.setup_log_panel(main_frame)
        
    def setup_score_display(self, parent):
        score_frame = tk.LabelFrame(
            parent, 
            text="Battle Scores", 
            font=("Arial", 12, "bold"),
            fg='#ffffff',
            bg='#2d2d2d',
            bd=2
        )
        score_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        scores_inner = tk.Frame(score_frame, bg='#2d2d2d')
        scores_inner.pack(fill=tk.X, padx=10, pady=5)
        
        # Blue team score
        tk.Label(
            scores_inner, 
            text="🛡️ Blue Team:", 
            font=("Arial", 11, "bold"),
            fg='#4a9eff',
            bg='#2d2d2d'
        ).pack(side=tk.LEFT)
        
        self.blue_score_label = tk.Label(
            scores_inner, 
            text="0", 
            font=("Arial", 14, "bold"),
            fg='#4a9eff',
            bg='#2d2d2d'
        )
        self.blue_score_label.pack(side=tk.LEFT, padx=(5, 20))
        
        # Red team score
        tk.Label(
            scores_inner, 
            text="🔴 Red Team AI:", 
            font=("Arial", 11, "bold"),
            fg='#ff4a4a',
            bg='#2d2d2d'
        ).pack(side=tk.LEFT)
        
        self.red_score_label = tk.Label(
            scores_inner, 
            text="0", 
            font=("Arial", 14, "bold"),
            fg='#ff4a4a',
            bg='#2d2d2d'
        )
        self.red_score_label.pack(side=tk.LEFT, padx=5)
        
        # Round counter
        tk.Label(
            scores_inner, 
            text="Round:", 
            font=("Arial", 11, "bold"),
            fg='#ffffff',
            bg='#2d2d2d'
        ).pack(side=tk.RIGHT, padx=(20, 5))
        
        self.round_label = tk.Label(
            scores_inner, 
            text="0", 
            font=("Arial", 14, "bold"),
            fg='#ffff00',
            bg='#2d2d2d'
        )
        self.round_label.pack(side=tk.RIGHT)
        
    def setup_game_controls(self, parent):
        control_frame = tk.LabelFrame(
            parent, 
            text="Game Controls", 
            font=("Arial", 12, "bold"),
            fg='#ffffff',
            bg='#2d2d2d',
            bd=2
        )
        control_frame.pack(side=tk.RIGHT, padx=(10, 0))
        
        controls_inner = tk.Frame(control_frame, bg='#2d2d2d')
        controls_inner.pack(padx=10, pady=5)
        
        self.start_button = tk.Button(
            controls_inner,
            text="🚀 Start Battle",
            command=self.start_game,
            bg='#00aa00',
            fg='white',
            font=("Arial", 10, "bold"),
            width=12
        )
        self.start_button.pack(side=tk.LEFT, padx=(0, 5))
        
        self.pause_button = tk.Button(
            controls_inner,
            text="⏸️ Pause",
            command=self.toggle_pause,
            bg='#ffaa00',
            fg='white',
            font=("Arial", 10, "bold"),
            width=8,
            state=tk.DISABLED
        )
        self.pause_button.pack(side=tk.LEFT, padx=5)
        
        self.reset_button = tk.Button(
            controls_inner,
            text="🔄 Reset",
            command=self.reset_game,
            bg='#aa0000',
            fg='white',
            font=("Arial", 10, "bold"),
            width=8
        )
        self.reset_button.pack(side=tk.LEFT, padx=(5, 0))
        
    def setup_system_state(self, parent):
        state_frame = tk.LabelFrame(
            parent,
            text="🏢 System Status",
            font=("Arial", 12, "bold"),
            fg='#ffffff',
            bg='#2d2d2d',
            bd=2
        )
        state_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Vulnerabilities display
        vuln_frame = tk.Frame(state_frame, bg='#2d2d2d')
        vuln_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(
            vuln_frame,
            text="🔓 Vulnerabilities:",
            font=("Arial", 11, "bold"),
            fg='#ffaa00',
            bg='#2d2d2d'
        ).pack(anchor=tk.W)
        
        self.vuln_progress = ttk.Progressbar(
            vuln_frame,
            length=200,
            mode='determinate'
        )
        self.vuln_progress.pack(fill=tk.X, pady=5)
        
        self.vuln_label = tk.Label(
            vuln_frame,
            text="3/3",
            font=("Arial", 10),
            fg='#ffffff',
            bg='#2d2d2d'
        )
        self.vuln_label.pack(anchor=tk.W)
        
        # Detection level display
        detect_frame = tk.Frame(state_frame, bg='#2d2d2d')
        detect_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(
            detect_frame,
            text="🔍 Detection Level:",
            font=("Arial", 11, "bold"),
            fg='#4a9eff',
            bg='#2d2d2d'
        ).pack(anchor=tk.W)
        
        self.detect_progress = ttk.Progressbar(
            detect_frame,
            length=200,
            mode='determinate'
        )
        self.detect_progress.pack(fill=tk.X, pady=5)
        
        self.detect_label = tk.Label(
            detect_frame,
            text="0/5",
            font=("Arial", 10),
            fg='#ffffff',
            bg='#2d2d2d'
        )
        self.detect_label.pack(anchor=tk.W)
        
        # System status
        status_frame = tk.Frame(state_frame, bg='#2d2d2d')
        status_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(
            status_frame,
            text="🖥️ System Status:",
            font=("Arial", 11, "bold"),
            fg='#ffffff',
            bg='#2d2d2d'
        ).pack(anchor=tk.W)
        
        self.status_label = tk.Label(
            status_frame,
            text="🟢 SECURE",
            font=("Arial", 12, "bold"),
            fg='#00ff00',
            bg='#2d2d2d'
        )
        self.status_label.pack(anchor=tk.W, pady=5)
        
    def setup_action_controls(self, parent):
        action_frame = tk.LabelFrame(
            parent,
            text="🛡️ Blue Team Actions",
            font=("Arial", 12, "bold"),
            fg='#4a9eff',
            bg='#2d2d2d',
            bd=2
        )
        action_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        
        # Action buttons
        self.action_buttons = {}
        actions = [
            ("🔧 Patch System", "patch", "#00aa00"),
            ("👁️ Monitor Network", "monitor", "#0066aa"),
            ("🚫 Block Traffic", "block", "#aa6600"),
            ("🔒 Strengthen Security", "strengthen", "#6600aa"),
            ("📊 Analyze Logs", "analyze", "#aa0066")
        ]
        
        for i, (text, action, color) in enumerate(actions):
            btn = tk.Button(
                action_frame,
                text=text,
                command=lambda a=action: self.blue_team_action(a),
                bg=color,
                fg='white',
                font=("Arial", 10, "bold"),
                width=20,
                height=2,
                state=tk.DISABLED
            )
            btn.pack(pady=5, padx=10, fill=tk.X)
            self.action_buttons[action] = btn
        
        # AI Action Display
        ai_frame = tk.LabelFrame(
            action_frame,
            text="🔴 Red Team AI Last Action",
            font=("Arial", 10, "bold"),
            fg='#ff4a4a',
            bg='#2d2d2d'
        )
        ai_frame.pack(fill=tk.X, padx=10, pady=(10, 5))
        
        self.ai_action_label = tk.Label(
            ai_frame,
            text="Waiting...",
            font=("Arial", 11),
            fg='#ffffff',
            bg='#2d2d2d',
            wraplength=200
        )
        self.ai_action_label.pack(pady=5)
        
    def setup_statistics_panel(self, parent):
        stats_frame = tk.LabelFrame(
            parent,
            text="📊 Battle Statistics",
            font=("Arial", 12, "bold"),
            fg='#ffffff',
            bg='#2d2d2d',
            bd=2
        )
        stats_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Overall statistics
        overall_frame = tk.Frame(stats_frame, bg='#2d2d2d')
        overall_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(
            overall_frame,
            text="🏆 Overall Stats",
            font=("Arial", 11, "bold"),
            fg='#ffff00',
            bg='#2d2d2d'
        ).pack(anchor=tk.W)
        
        self.total_rounds_label = tk.Label(
            overall_frame,
            text="Total Rounds: 0",
            font=("Arial", 9),
            fg='#ffffff',
            bg='#2d2d2d'
        )
        self.total_rounds_label.pack(anchor=tk.W)
        
        self.blue_wins_label = tk.Label(
            overall_frame,
            text="Blue Wins: 0 (0%)",
            font=("Arial", 9),
            fg='#4a9eff',
            bg='#2d2d2d'
        )
        self.blue_wins_label.pack(anchor=tk.W)
        
        self.red_wins_label = tk.Label(
            overall_frame,
            text="Red Wins: 0 (0%)",
            font=("Arial", 9),
            fg='#ff4a4a',
            bg='#2d2d2d'
        )
        self.red_wins_label.pack(anchor=tk.W)
        
        # AI Learning Progress
        learning_frame = tk.Frame(stats_frame, bg='#2d2d2d')
        learning_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(
            learning_frame,
            text="🧠 AI Learning Progress",
            font=("Arial", 11, "bold"),
            fg='#ff4a4a',
            bg='#2d2d2d'
        ).pack(anchor=tk.W)
        
        self.learning_progress = ttk.Progressbar(
            learning_frame,
            length=150,
            mode='determinate'
        )
        self.learning_progress.pack(fill=tk.X, pady=5)
        
        self.q_table_size_label = tk.Label(
            learning_frame,
            text="States Learned: 0",
            font=("Arial", 9),
            fg='#ffffff',
            bg='#2d2d2d'
        )
        self.q_table_size_label.pack(anchor=tk.W)
        
        # Performance metrics
        perf_frame = tk.Frame(stats_frame, bg='#2d2d2d')
        perf_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(
            perf_frame,
            text="⚡ Performance",
            font=("Arial", 11, "bold"),
            fg='#00ff00',
            bg='#2d2d2d'
        ).pack(anchor=tk.W)
        
        self.avg_time_label = tk.Label(
            perf_frame,
            text="Avg Round Time: 0s",
            font=("Arial", 9),
            fg='#ffffff',
            bg='#2d2d2d'
        )
        self.avg_time_label.pack(anchor=tk.W)
        
        self.difficulty_label = tk.Label(
            perf_frame,
            text="Difficulty: Adaptive",
            font=("Arial", 9),
            fg='#ffffff',
            bg='#2d2d2d'
        )
        self.difficulty_label.pack(anchor=tk.W)
        
    def setup_log_panel(self, parent):
        log_frame = tk.LabelFrame(
            parent,
            text="📋 Battle Log",
            font=("Arial", 12, "bold"),
            fg='#ffffff',
            bg='#2d2d2d',
            bd=2
        )
        log_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            height=8,
            bg='#1a1a1a',
            fg='#00ff00',
            font=("Consolas", 9),
            wrap=tk.WORD
        )
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Configure text tags for different log types
        self.log_text.tag_configure("red_action", foreground="#ff6b6b")
        self.log_text.tag_configure("blue_action", foreground="#4a9eff")
        self.log_text.tag_configure("system", foreground="#ffff00")
        self.log_text.tag_configure("warning", foreground="#ff8c00")
        self.log_text.tag_configure("success", foreground="#00ff00")
        
    def start_game(self):
        if not self.game_running:
            self.game_running = True
            self.game_paused = False
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            
            # Enable action buttons
            for btn in self.action_buttons.values():
                btn.config(state=tk.NORMAL)
            
            self.log_message("🚀 Battle initiated! Blue Team vs Red Team AI", "system")
            
            # Start game loop in separate thread
            threading.Thread(target=self.game_loop, daemon=True).start()
    
    def toggle_pause(self):
        self.game_paused = not self.game_paused
        if self.game_paused:
            self.pause_button.config(text="▶️ Resume")
            self.log_message("⏸️ Battle paused", "system")
        else:
            self.pause_button.config(text="⏸️ Pause")
            self.log_message("▶️ Battle resumed", "system")
    
    def reset_game(self):
        self.game_running = False
        self.game_paused = False
        self.round_count = 0
        self.blue_score = 0
        self.red_score = 0
        
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED, text="⏸️ Pause")
        
        # Disable action buttons
        for btn in self.action_buttons.values():
            btn.config(state=tk.DISABLED)
        
        # Reset environment
        self.environment = Environment()
        self.red_ai = RedTeamAI(actions=["scan", "exploit", "brute_force", "social_engineering"])
        
        # Clear log
        self.log_text.delete(1.0, tk.END)
        
        self.update_display()
        self.log_message("🔄 Battle arena reset", "system")
    
    def blue_team_action(self, action):
        if self.game_running and not self.game_paused:
            self.selected_blue_action = action
            self.log_message(f"🛡️ Blue Team executed: {action.upper()}", "blue_action")
    
    def game_loop(self):
        while self.game_running:
            if self.game_paused:
                time.sleep(0.1)
                continue
                
            self.round_count += 1
            self.total_rounds += 1
            round_start_time = time.time()
            
            # Reset environment for new round
            state = self.environment.reset()
            self.selected_blue_action = None
            
            self.root.after(0, self.update_display)
            self.root.after(0, lambda: self.log_message(f"\n=== 🔥 ROUND {self.round_count} 🔥 ===", "system"))
            
            step_count = 0
            while not state["breach"] and state["detection"] <= 4 and self.game_running:
                if self.game_paused:
                    time.sleep(0.1)
                    continue
                
                step_count += 1
                
                # Wait for blue team action
                self.root.after(0, lambda: self.log_message("⏳ Waiting for Blue Team action...", "blue_action"))
                while self.selected_blue_action is None and self.game_running and not self.game_paused:
                    time.sleep(0.1)
                
                if not self.game_running:
                    break
                
                blue_action = self.selected_blue_action
                self.selected_blue_action = None
                
                # Red team AI action
                red_action = self.red_ai.choose_action(state)
                self.root.after(0, lambda a=red_action: self.ai_action_label.config(text=f"🔴 {a.upper()}"))
                self.root.after(0, lambda a=red_action: self.log_message(f"🔴 Red Team AI executed: {a.upper()}", "red_action"))
                
                # Execute actions
                next_state, reward = self.environment.step(red_action, blue_action)
                self.red_ai.learn(state, red_action, reward, next_state)
                
                state = next_state
                self.root.after(0, self.update_display)
                
                # Check win conditions
                if state["breach"]:
                    self.red_score += 1
                    self.red_wins += 1
                    self.root.after(0, lambda: self.log_message("🚨 SYSTEM BREACHED! Red Team AI wins this round!", "warning"))
                    break
                elif state["detection"] > 4:
                    self.blue_score += 1
                    self.blue_wins += 1
                    self.root.after(0, lambda: self.log_message("✅ THREAT NEUTRALIZED! Blue Team wins this round!", "success"))
                    break
                
                time.sleep(1)  # Pause between steps
            
            # Update round statistics
            round_time = time.time() - round_start_time
            if self.total_rounds > 0:
                self.avg_detection_time = (self.avg_detection_time * (self.total_rounds - 1) + round_time) / self.total_rounds
            
            self.root.after(0, self.update_statistics)
            time.sleep(2)  # Pause between rounds
    
    def update_display(self):
        state = self.environment.state
        
        # Update vulnerabilities progress bar
        vuln_percentage = (state["vulnerabilities"] / 3) * 100
        self.vuln_progress['value'] = vuln_percentage
        self.vuln_label.config(text=f"{state['vulnerabilities']}/3")
        
        # Update detection progress bar
        detect_percentage = (state["detection"] / 5) * 100
        self.detect_progress['value'] = detect_percentage
        self.detect_label.config(text=f"{state['detection']}/5")
        
        # Update system status
        if state["breach"]:
            self.status_label.config(text="🔴 BREACHED", fg='#ff0000')
        elif state["detection"] > 3:
            self.status_label.config(text="🟡 HIGH ALERT", fg='#ffff00')
        elif state["vulnerabilities"] < 2:
            self.status_label.config(text="🟡 VULNERABLE", fg='#ffaa00')
        else:
            self.status_label.config(text="🟢 SECURE", fg='#00ff00')
        
        # Update scores
        self.blue_score_label.config(text=str(self.blue_score))
        self.red_score_label.config(text=str(self.red_score))
        self.round_label.config(text=str(self.round_count))
    
    def update_statistics(self):
        # Update overall statistics
        self.total_rounds_label.config(text=f"Total Rounds: {self.total_rounds}")
        
        if self.total_rounds > 0:
            blue_win_rate = (self.blue_wins / self.total_rounds) * 100
            red_win_rate = (self.red_wins / self.total_rounds) * 100
            
            self.blue_wins_label.config(text=f"Blue Wins: {self.blue_wins} ({blue_win_rate:.1f}%)")
            self.red_wins_label.config(text=f"Red Wins: {self.red_wins} ({red_win_rate:.1f}%)")
        
        # Update AI learning progress
        q_table_size = len(self.red_ai.q_table)
        learning_progress = min(q_table_size * 10, 100)  # Cap at 100%
        self.learning_progress['value'] = learning_progress
        self.q_table_size_label.config(text=f"States Learned: {q_table_size}")
        
        # Update performance metrics
        self.avg_time_label.config(text=f"Avg Round Time: {self.avg_detection_time:.1f}s")
    
    def log_message(self, message, tag=""):
        timestamp = time.strftime("%H:%M:%S")
        full_message = f"[{timestamp}] {message}\n"
        
        self.log_text.insert(tk.END, full_message, tag)
        self.log_text.see(tk.END)


def main():
    root = tk.Tk()
    app = CyberSecurityGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
