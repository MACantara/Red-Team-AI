# Red Team vs Blue Team AI Simulation

An interactive cybersecurity simulation featuring an AI-powered red team attacking a system defended by a human blue team player. The simulation now includes a comprehensive GUI and enhanced gamified mechanics.

## 🚀 Quick Start

### Easy Launch (Recommended)
```bash
python launcher.py
```
The launcher provides a simple interface to choose between different simulation modes.

### Direct Launch Options
- **GUI Human vs AI**: `python gui_game.py`
- **Auto AI vs AI Battle**: `python auto_gui_game.py`
- **Console Mode**: `python main.py`

## Features

### 🎮 Enhanced Gamified Mechanics
- **Real-time Battle Arena**: Interactive GUI with live updates
- **Adaptive AI**: Red team AI that learns and adapts strategies
- **Multiple Defense Actions**: 5 different blue team defensive strategies
- **Dynamic Difficulty**: Game difficulty adapts based on AI learning
- **Performance Tracking**: Comprehensive statistics and win rates
- **Speed Control**: Adjustable game speed in auto mode (0.1x to 5x)

### 🛡️ Blue Team Actions
1. **🔧 Patch System**: Fix vulnerabilities in the system
2. **👁️ Monitor Network**: Increase detection capabilities
3. **🚫 Block Traffic**: Block suspicious network traffic
4. **🔒 Strengthen Security**: Improve overall security posture
5. **📊 Analyze Logs**: Analyze system logs for attack patterns

### 🔴 Red Team AI Strategies
- **Scanning**: Gather information about the target system
- **Exploitation**: Exploit discovered vulnerabilities
- **Brute Force**: Attempt to overwhelm security measures
- **Social Engineering**: Bypass technical defenses through human factors

### 🧠 AI Learning Features
- **Q-Learning Algorithm**: AI improves performance over time
- **Strategic Adaptation**: Switches between stealth, aggressive, and adaptive strategies
- **State Awareness**: Considers multiple environmental factors
- **Dynamic Exploration**: Balanced exploration vs exploitation

## Installation

1. Ensure Python 3.8+ is installed
2. Clone or download this repository
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Game Modes

### 1. GUI Mode (Human vs AI) 🎮
- **Launch**: `python gui_game.py` or via launcher
- **Features**: Interactive GUI where you control the Blue Team
- **Best For**: Learning cybersecurity concepts and strategies

### 2. Auto Battle Mode (AI vs AI) 🤖
- **Launch**: `python auto_gui_game.py` or via launcher
- **Features**: Watch AI vs AI battles with speed controls
- **Best For**: Observing AI learning patterns and long-term simulations

### 3. Console Mode 💻
- **Launch**: `python main.py` or via launcher
- **Features**: Traditional text-based interface
- **Best For**: Focused gameplay and debugging

## Game Mechanics

### Winning Conditions
- **Red Team Wins**: Successfully breach the system
- **Blue Team Wins**: Detect and neutralize the threat (detection > 4)

### System State Variables
- **Vulnerabilities**: Number of exploitable weaknesses (0-5, adaptive)
- **Detection Level**: Current threat detection capability (0-5)
- **Security Level**: Overall system security strength (0-10)
- **Network Activity**: Level of suspicious network traffic (0-5)
- **Breach Status**: Whether the system has been compromised
- **Logs Analyzed**: Whether security logs have been examined

### Scoring System
- Blue team gains points for successful threat neutralization
- Red team gains points for successful system breaches
- Performance statistics track long-term success rates

## Advanced Features

### Adaptive Difficulty System
- **Dynamic Vulnerabilities**: Base vulnerabilities increase as AI learns
  - Round 20+: Chance for 4 initial vulnerabilities
  - Round 50+: Chance for 5 initial vulnerabilities
- **Strategic Evolution**: AI strategies become more sophisticated over time
- **Balanced Challenge**: Detection mechanisms adapt to common attack patterns

### AI Strategy Selection
The Red Team AI dynamically chooses between three strategies:

1. **Stealth Mode** 🥷
   - Activated when detection levels are high (>3)
   - Prefers low-detection actions (scan, social_engineering)
   - Minimizes risk of discovery

2. **Aggressive Mode** ⚔️
   - Activated when vulnerabilities are high and detection is low
   - Prefers high-reward actions (exploit, brute_force)
   - Maximizes damage potential

3. **Adaptive Mode** 🧠
   - Default balanced approach
   - Switches between strategies based on context
   - Optimizes for long-term success

### Performance Analytics
- **Real-time Learning Progress**: Visual representation of AI improvement
- **Win Rate Tracking**: Long-term performance trends
- **Strategy Distribution**: Analysis of AI decision patterns
- **Speed Metrics**: Average round completion times

## File Structure
```
Red-Team-AI/
├── launcher.py          # Easy-to-use launcher interface
├── gui_game.py         # Main GUI application (Human vs AI)
├── auto_gui_game.py    # Auto battle GUI (AI vs AI)
├── main.py            # Console-based version
├── environment.py     # Enhanced game environment and mechanics
├── ai.py             # Advanced red team AI with Q-learning
├── player.py         # Blue team player classes (human & AI)
├── requirements.txt  # Python dependencies
└── README.md        # This documentation
```

## Tips for Blue Team Players

### Strategic Priorities
1. **Vulnerability Management**: Always prioritize patching when vulnerabilities > 2
2. **Active Monitoring**: Maintain high detection during suspicious activity
3. **Log Analysis**: Use during active attacks for maximum detection boost
4. **Proactive Security**: Strengthen defenses during quiet periods
5. **Traffic Management**: Use blocking sparingly to avoid legitimate impact

### Advanced Tactics
- **Pattern Recognition**: Learn to identify AI strategy shifts
- **Resource Optimization**: Balance immediate threats vs long-term security
- **Timing**: Coordinate defensive actions for maximum effectiveness

## AI Learning Progress

The red team AI learns through multiple mechanisms:

### Learning Components
- **Experience Replay**: Remembers and learns from past encounters
- **Reward Shaping**: Optimizes for both stealth and effectiveness
- **Strategy Coherence**: Maintains consistent tactical approaches
- **Environmental Adaptation**: Adjusts to changing security conditions

### Learning Indicators
- **Q-Table Growth**: Number of state-action pairs learned
- **Epsilon Decay**: Reduction in random exploration over time
- **Strategy Evolution**: Changes in preferred action patterns
- **Performance Improvement**: Increasing win rates over time

## Technical Details

### Dependencies
- **Python**: 3.8 or higher
- **tkinter**: GUI framework (usually included with Python)
- **numpy**: Mathematical operations for AI
- **threading**: Concurrent GUI updates

### Performance Considerations
- Game speed adjustable from 0.1x to 5x normal speed
- Memory efficient Q-learning implementation
- Responsive GUI with background processing
- Optimized for long-running simulations

## Educational Value

This simulation provides hands-on experience with:
- **Cybersecurity Concepts**: Attack/defense strategies
- **AI/ML Principles**: Reinforcement learning in action
- **Game Theory**: Strategic decision making
- **Risk Assessment**: Balancing security measures
- **Pattern Recognition**: Identifying attack signatures

## Contributing

Contributions welcome for:
- New attack/defense strategies
- GUI improvements and features
- AI learning algorithm enhancements
- Performance optimizations
- Documentation improvements

## Future Enhancements

Planned features:
- **Multi-stage Attacks**: Complex attack chains
- **Team Play**: Multiple defenders vs multiple attackers
- **Network Topology**: Realistic network layouts
- **Threat Intelligence**: Real-world attack patterns
- **Reporting System**: Detailed post-game analysis

## License

This project is designed for educational purposes in cybersecurity training and AI development.

---

## Getting Started Example

1. **Install and Launch**:
   ```bash
   pip install -r requirements.txt
   python launcher.py
   ```

2. **Choose GUI Mode** for your first game

3. **Start with basic strategy**:
   - Patch vulnerabilities when they appear
   - Monitor network activity regularly
   - Analyze logs during suspicious activity

4. **Observe AI behavior** and adapt your strategy

5. **Try Auto Battle Mode** to see AI vs AI learning

Enjoy exploring the dynamic world of cybersecurity simulation! 🛡️🔴
