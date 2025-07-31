import random
from typing import Dict, List

class BlueTeamPlayer:
    def __init__(self):
        self.actions = ["patch", "monitor", "block", "strengthen", "analyze"]
        self.action_descriptions = {
            "patch": "Fix vulnerabilities in the system",
            "monitor": "Increase network monitoring and detection capabilities",
            "block": "Block suspicious network traffic (may affect legitimate users)",
            "strengthen": "Strengthen overall security posture",
            "analyze": "Analyze system logs for attack patterns"
        }
        self.action_history = []
        self.performance_stats = {
            "actions_taken": 0,
            "successful_defenses": 0,
            "rounds_won": 0
        }

    def choose_action(self):
        """Basic implementation for console-based interaction"""
        print("\nBlue Team Actions:")
        for i, action in enumerate(self.actions):
            print(f"{i+1}. {action.title()} - {self.action_descriptions[action]}")
        
        while True:
            try:
                choice = int(input("Choose your action (1-5): ")) - 1
                if 0 <= choice < len(self.actions):
                    action = self.actions[choice]
                    self.record_action(action)
                    return action
                else:
                    print("Invalid choice. Please select 1-5.")
            except ValueError:
                print("Please enter a valid number.")

    def record_action(self, action: str):
        """Record action for performance tracking"""
        self.action_history.append(action)
        self.performance_stats["actions_taken"] += 1
        
        # Keep history manageable
        if len(self.action_history) > 50:
            self.action_history.pop(0)

    def get_action_recommendation(self, state: Dict) -> str:
        """AI-assisted recommendation for blue team actions"""
        recommendations = []
        
        # High priority: patch vulnerabilities
        if state.get("vulnerabilities", 0) > 2:
            recommendations.append(("patch", 0.9, "High vulnerability count detected"))
        
        # High priority: monitor when suspicious activity
        if state.get("network_activity", 0) > 2:
            recommendations.append(("monitor", 0.8, "Suspicious network activity detected"))
        
        # Medium priority: analyze logs during attacks
        if state.get("network_activity", 0) > 0 and not state.get("logs_analyzed", False):
            recommendations.append(("analyze", 0.7, "Attack in progress - analyze logs"))
        
        # Medium priority: strengthen security if detection is low
        if state.get("detection", 0) < 2 and state.get("security_level", 0) < 4:
            recommendations.append(("strengthen", 0.6, "Low detection capability"))
        
        # Low priority: block traffic if under active attack
        if state.get("detection", 0) > 3:
            recommendations.append(("block", 0.5, "High threat detection level"))
        
        if not recommendations:
            # Default recommendations based on current state
            if state.get("vulnerabilities", 0) > 0:
                return "patch"
            else:
                return "monitor"
        
        # Return highest priority recommendation
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return recommendations[0][0]

    def get_performance_summary(self) -> Dict:
        """Get summary of player performance"""
        return {
            "total_actions": self.performance_stats["actions_taken"],
            "successful_defenses": self.performance_stats["successful_defenses"],
            "rounds_won": self.performance_stats["rounds_won"],
            "win_rate": (self.performance_stats["rounds_won"] / max(1, self.performance_stats["actions_taken"] // 10)) * 100,
            "recent_actions": self.action_history[-10:] if self.action_history else []
        }


class AutoBlueTeamPlayer(BlueTeamPlayer):
    """Automated Blue Team player for continuous gameplay"""
    
    def __init__(self, difficulty="medium"):
        super().__init__()
        self.difficulty = difficulty
        self.decision_weights = self.get_difficulty_weights()
        
    def get_difficulty_weights(self) -> Dict[str, float]:
        """Get decision-making weights based on difficulty"""
        if self.difficulty == "easy":
            return {
                "reactive": 0.8,    # Mostly reactive to immediate threats
                "proactive": 0.2,   # Some proactive measures
                "optimal": 0.1      # Rarely optimal decisions
            }
        elif self.difficulty == "medium":
            return {
                "reactive": 0.6,
                "proactive": 0.3,
                "optimal": 0.3
            }
        else:  # hard
            return {
                "reactive": 0.4,
                "proactive": 0.4,
                "optimal": 0.6
            }
    
    def choose_action(self, state: Dict = None) -> str:
        """Automatically choose action based on state and difficulty"""
        if state is None:
            return random.choice(self.actions)
        
        # Use optimal strategy based on difficulty
        if random.random() < self.decision_weights["optimal"]:
            action = self.get_action_recommendation(state)
        elif random.random() < self.decision_weights["proactive"]:
            action = self.get_proactive_action(state)
        else:
            action = self.get_reactive_action(state)
        
        self.record_action(action)
        return action
    
    def get_proactive_action(self, state: Dict) -> str:
        """Choose proactive defensive actions"""
        # Strengthen security when things are calm
        if state.get("detection", 0) < 2 and state.get("network_activity", 0) < 2:
            if state.get("security_level", 0) < 5:
                return "strengthen"
            elif not state.get("logs_analyzed", False):
                return "analyze"
        
        # Default to monitoring
        return "monitor"
    
    def get_reactive_action(self, state: Dict) -> str:
        """Choose reactive actions based on immediate threats"""
        # React to high vulnerability count
        if state.get("vulnerabilities", 0) > 1:
            return "patch"
        
        # React to suspicious activity
        if state.get("network_activity", 0) > 1:
            return "monitor"
        
        # Random action if no clear threat
        return random.choice(self.actions)
