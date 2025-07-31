import random

class Environment:
    def __init__(self):
        self.state = {
            "vulnerabilities": 3,  # Number of vulnerabilities
            "detection": 0,        # Detection level
            "breach": False,       # Red team success flag
            "security_level": 3,   # Overall security strength
            "network_activity": 0, # Suspicious network activity level
            "logs_analyzed": False # Whether logs have been analyzed this round
        }
        self.max_vulnerabilities = 3
        self.max_detection = 5
        self.round_count = 0

    def reset(self):
        self.round_count += 1
        # Adaptive difficulty - occasionally add more vulnerabilities as AI learns
        base_vulns = 3
        if self.round_count > 20 and random.random() < 0.3:
            base_vulns = 4
        elif self.round_count > 50 and random.random() < 0.2:
            base_vulns = 5
            
        self.max_vulnerabilities = base_vulns
        self.state = {
            "vulnerabilities": base_vulns, 
            "detection": 0, 
            "breach": False,
            "security_level": 3,
            "network_activity": 0,
            "logs_analyzed": False
        }
        return self.state

    def step(self, red_action, blue_action):
        reward = 0
        detection_increase = 0

        # Blue team actions with enhanced mechanics
        if blue_action == "patch" and self.state["vulnerabilities"] > 0:
            self.state["vulnerabilities"] -= 1
            self.state["security_level"] += 1
            detection_increase = 0  # Patching doesn't increase detection directly
            
        elif blue_action == "monitor":
            self.state["detection"] += 2
            detection_increase = 2
            if self.state["network_activity"] > 0:
                self.state["detection"] += 1  # Extra detection if there's suspicious activity
                detection_increase += 1
                
        elif blue_action == "block":
            reward -= 2  # Penalty for potentially blocking legitimate traffic
            self.state["detection"] += 1
            detection_increase = 1
            if self.state["network_activity"] > 2:
                self.state["network_activity"] -= 1  # Reduce suspicious activity
                
        elif blue_action == "strengthen":
            self.state["security_level"] += 2
            # Strengthening security can reveal vulnerabilities
            if random.random() < 0.4 and self.state["vulnerabilities"] < self.max_vulnerabilities:
                self.state["vulnerabilities"] += 1
                
        elif blue_action == "analyze":
            self.state["logs_analyzed"] = True
            if self.state["network_activity"] > 0:
                self.state["detection"] += 3  # Big detection boost if analyzing during attack
                detection_increase = 3

        # Red team actions with enhanced mechanics
        detection_risk = 0
        
        if red_action == "scan":
            reward += 1
            self.state["network_activity"] += 1
            detection_risk = 1
            if self.state["logs_analyzed"]:
                detection_risk += 2  # Higher risk if logs are being analyzed
                
        elif red_action == "exploit" and self.state["vulnerabilities"] > 0:
            self.state["vulnerabilities"] -= 1
            self.state["network_activity"] += 2
            reward += 5
            detection_risk = 2
            
            # Success depends on security level
            exploit_success = random.random()
            security_modifier = self.state["security_level"] * 0.1
            
            if exploit_success > security_modifier:
                if self.state["vulnerabilities"] == 0:
                    self.state["breach"] = True
                    reward += 15
            else:
                reward -= 2  # Failed exploit
                detection_risk += 1
                
        elif red_action == "brute_force":
            self.state["network_activity"] += 3
            detection_risk = 3
            # Brute force success inversely related to security level
            success_chance = max(0.1, 0.5 - (self.state["security_level"] * 0.1))
            if random.random() < success_chance:
                self.state["breach"] = True
                reward += 12
            else:
                reward -= 3  # Failed brute force
                detection_risk += 2
                
        elif red_action == "social_engineering":
            # Social engineering bypasses some technical defenses
            self.state["network_activity"] += 1
            detection_risk = 1
            # Success chance is less affected by security level
            if random.random() < 0.35:
                self.state["breach"] = True
                reward += 10
                # Social engineering might reveal vulnerabilities
                if random.random() < 0.3 and self.state["vulnerabilities"] < self.max_vulnerabilities:
                    self.state["vulnerabilities"] += 1

        # Apply detection risk
        if random.random() < (detection_risk * 0.3):
            self.state["detection"] += detection_risk

        # Detection penalties for red team
        if self.state["detection"] > 2:
            reward -= (self.state["detection"] - 2) * 2
        
        # Bonus for maintaining stealth
        if self.state["detection"] == 0 and self.state["network_activity"] > 0:
            reward += 1

        # Cap detection at maximum
        self.state["detection"] = min(self.state["detection"], self.max_detection)
        
        # Network activity naturally decreases over time
        if self.state["network_activity"] > 0:
            self.state["network_activity"] = max(0, self.state["network_activity"] - 1)

        return self.state, reward
