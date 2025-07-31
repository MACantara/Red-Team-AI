import random
import numpy as np

class RedTeamAI:
    def __init__(self, actions):
        self.q_table = {}  # state-action values
        self.actions = actions
        self.alpha = 0.1    # learning rate
        self.gamma = 0.9    # discount factor
        self.epsilon = 0.3  # exploration rate
        self.epsilon_decay = 0.995  # epsilon decay rate
        self.epsilon_min = 0.05     # minimum epsilon
        
        # Enhanced state tracking
        self.action_history = []
        self.reward_history = []
        self.episode_count = 0
        
        # Strategy weights for different scenarios
        self.strategy_weights = {
            "stealth": 0.7,     # Prefer low-detection actions
            "aggressive": 0.3,  # Prefer high-reward actions
            "adaptive": 0.5     # Balance between stealth and aggression
        }
        self.current_strategy = "adaptive"

    def get_state_key(self, state):
        # Enhanced state representation including more factors
        return f"{state['vulnerabilities']}_{state['detection']}_{state['security_level']}_{state['network_activity']}"

    def choose_action(self, state):
        state_key = self.get_state_key(state)
        
        # Adaptive strategy selection based on game state
        self.adapt_strategy(state)
        
        # Epsilon-greedy with strategy influence
        if random.random() < self.epsilon or state_key not in self.q_table:
            return self.choose_strategic_action(state)
        
        # Choose best action based on Q-values and current strategy
        q_values = self.q_table[state_key]
        
        if self.current_strategy == "stealth":
            # Prefer actions with lower detection risk
            stealth_actions = ["scan", "social_engineering"]
            stealth_q_values = {action: q_values.get(action, 0) for action in stealth_actions if action in self.actions}
            if stealth_q_values and random.random() < 0.7:
                return max(stealth_q_values, key=stealth_q_values.get)
                
        elif self.current_strategy == "aggressive":
            # Prefer high-reward actions
            aggressive_actions = ["exploit", "brute_force"]
            aggressive_q_values = {action: q_values.get(action, 0) for action in aggressive_actions if action in self.actions}
            if aggressive_q_values and random.random() < 0.7:
                return max(aggressive_q_values, key=aggressive_q_values.get)
        
        # Default: choose action with highest Q-value
        return max(q_values, key=q_values.get)

    def choose_strategic_action(self, state):
        """Choose action based on current strategy when exploring"""
        if self.current_strategy == "stealth" and state["detection"] > 2:
            # Prefer low-risk actions when detection is high
            low_risk_actions = ["scan", "social_engineering"]
            available_low_risk = [action for action in low_risk_actions if action in self.actions]
            if available_low_risk:
                return random.choice(available_low_risk)
                
        elif self.current_strategy == "aggressive" and state["vulnerabilities"] > 0:
            # Prefer exploit when vulnerabilities exist
            if "exploit" in self.actions:
                return "exploit"
                
        # Default random choice
        return random.choice(self.actions)

    def adapt_strategy(self, state):
        """Dynamically adapt strategy based on game state"""
        # Switch to stealth mode if detection is high
        if state["detection"] > 3:
            self.current_strategy = "stealth"
        # Switch to aggressive if vulnerabilities are high and detection is low
        elif state["vulnerabilities"] > 2 and state["detection"] < 2:
            self.current_strategy = "aggressive"
        # Use adaptive strategy in balanced situations
        else:
            self.current_strategy = "adaptive"

    def learn(self, state, action, reward, next_state):
        state_key = self.get_state_key(state)
        next_key = self.get_state_key(next_state)

        # Initialize Q-table entries if they don't exist
        if state_key not in self.q_table:
            self.q_table[state_key] = {a: 0 for a in self.actions}
        if next_key not in self.q_table:
            self.q_table[next_key] = {a: 0 for a in self.actions}

        # Q-learning update with enhanced reward shaping
        current_q = self.q_table[state_key][action]
        max_future_q = max(self.q_table[next_key].values())
        
        # Add bonus for strategic coherence
        strategy_bonus = self.get_strategy_bonus(action, state)
        adjusted_reward = reward + strategy_bonus
        
        # Update Q-value
        new_q = current_q + self.alpha * (adjusted_reward + self.gamma * max_future_q - current_q)
        self.q_table[state_key][action] = new_q
        
        # Update history
        self.action_history.append(action)
        self.reward_history.append(reward)
        
        # Keep history manageable
        if len(self.action_history) > 100:
            self.action_history.pop(0)
            self.reward_history.pop(0)
        
        # Decay epsilon for less exploration over time
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def get_strategy_bonus(self, action, state):
        """Provide small bonus for strategically coherent actions"""
        bonus = 0
        
        if self.current_strategy == "stealth":
            if action in ["scan", "social_engineering"] and state["detection"] > 2:
                bonus = 0.5  # Bonus for choosing stealthy actions when detected
        elif self.current_strategy == "aggressive":
            if action in ["exploit", "brute_force"] and state["vulnerabilities"] > 0:
                bonus = 0.5  # Bonus for aggressive actions when vulnerabilities exist
                
        return bonus

    def get_learning_stats(self):
        """Return statistics about the AI's learning progress"""
        return {
            "states_learned": len(self.q_table),
            "epsilon": self.epsilon,
            "current_strategy": self.current_strategy,
            "avg_recent_reward": np.mean(self.reward_history[-10:]) if self.reward_history else 0
        }
