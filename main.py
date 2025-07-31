from environment import Environment
from ai import RedTeamAI
from player import BlueTeamPlayer

def main():
    print("🛡️ CYBERSECURITY SIMULATION - CONSOLE VERSION 🔴")
    print("=" * 50)
    
    env = Environment()
    ai = RedTeamAI(actions=["scan", "exploit", "brute_force", "social_engineering"])
    player = BlueTeamPlayer()
    
    blue_wins = 0
    red_wins = 0
    total_rounds = 0

    try:
        for episode in range(10):  # 10 rounds
            total_rounds += 1
            print(f"\n{'='*20} Round {episode+1} {'='*20}")
            state = env.reset()
            
            print(f"Initial State: {format_state(state)}")
            
            step_count = 0
            while not state["breach"] and state["detection"] <= 4:
                step_count += 1
                print(f"\n--- Step {step_count} ---")
                
                try:
                    blue_action = player.choose_action()
                    red_action = ai.choose_action(state)

                    print(f"🛡️ Blue Team chose: {blue_action}")
                    print(f"🔴 Red Team AI chose: {red_action}")
                    print(f"🧠 Red AI Strategy: {ai.current_strategy}")
                    
                    next_state, reward = env.step(red_action, blue_action)
                    ai.learn(state, red_action, reward, next_state)

                    state = next_state
                    print(f"📊 State: {format_state(state)}")
                    print(f"🎯 Red AI Reward: {reward}")
                    
                    if state["breach"]:
                        print("🚨 RED TEAM BREACHED THE SYSTEM!")
                        red_wins += 1
                        break
                    elif state["detection"] > 4:
                        print("✅ BLUE TEAM DETECTED AND STOPPED THE ATTACK!")
                        blue_wins += 1
                        break
                        
                except KeyboardInterrupt:
                    print("\n⏸️ Game interrupted by user")
                    break
                except Exception as e:
                    print(f"❌ Error during step: {e}")
                    break
                    
            # Round summary
            print(f"\n🏆 Round {episode+1} Complete!")
            if state["breach"]:
                print("🔴 Winner: Red Team AI")
            else:
                print("🛡️ Winner: Blue Team")
                
            # Display AI learning stats
            stats = ai.get_learning_stats()
            print(f"🧠 AI Learning Stats:")
            print(f"   States Learned: {stats['states_learned']}")
            print(f"   Exploration Rate: {stats['epsilon']:.2%}")
            print(f"   Current Strategy: {stats['current_strategy']}")
            print(f"   Avg Recent Reward: {stats['avg_recent_reward']:.2f}")
            
    except KeyboardInterrupt:
        print("\n🛑 Simulation terminated by user")
    
    # Final statistics
    print(f"\n{'='*50}")
    print("📊 FINAL STATISTICS")
    print(f"{'='*50}")
    print(f"Total Rounds: {total_rounds}")
    print(f"🛡️ Blue Team Wins: {blue_wins} ({(blue_wins/total_rounds)*100:.1f}%)")
    print(f"🔴 Red Team Wins: {red_wins} ({(red_wins/total_rounds)*100:.1f}%)")
    
    if blue_wins > red_wins:
        print("🎉 Blue Team is the overall winner!")
    elif red_wins > blue_wins:
        print("🎉 Red Team AI is the overall winner!")
    else:
        print("🤝 It's a tie!")
    
    # Display final AI stats
    final_stats = ai.get_learning_stats()
    print(f"\n🧠 Final AI Statistics:")
    print(f"   Total States Learned: {final_stats['states_learned']}")
    print(f"   Final Exploration Rate: {final_stats['epsilon']:.2%}")
    print(f"   Final Strategy: {final_stats['current_strategy']}")

def format_state(state):
    """Format state dictionary for better readability"""
    formatted = []
    for key, value in state.items():
        if key == "vulnerabilities":
            formatted.append(f"🔓 Vulns: {value}")
        elif key == "detection":
            formatted.append(f"🔍 Detection: {value}")
        elif key == "breach":
            formatted.append(f"🚨 Breach: {value}")
        elif key == "security_level":
            formatted.append(f"🔒 Security: {value}")
        elif key == "network_activity":
            formatted.append(f"📡 Activity: {value}")
        elif key == "logs_analyzed":
            formatted.append(f"📋 Logs: {value}")
    return " | ".join(formatted)

if __name__ == "__main__":
    main()
