import random

VALID_MOVES = ("rock", "paper", "scissors")

def counter_move(pred):
    if pred == "rock":
        return "paper"
    if pred == "paper":
        return "scissors"
    return "rock"

def winner(user, comp):
    if user == comp: return "tie"
    if (user == "rock" and comp == "scissors") or (user == "paper" and comp == "rock") or (user == "scissors" and comp == "paper"):
        return "win"
    return "lose"

def  predict_next_move(freqs):
    total = sum(freqs.values())
    if total == 0:
        return random.choice(VALID_MOVES), 0.0 # no data yet
    most = max(freqs, key=freqs.get)
    return most, freqs[most] / total

def play(): 
    print("=== Rock-Paper-Scissors Predictor - Part 2 (Stats) ===")
    print("Type rock/paper/scissors. Type 'exit' to stop.")
    freqs = {'rock': 0, 'paper': 0, 'scissors': 0}
    stats = {"wins": 0, "losses": 0, "ties": 0}
    rounds = 0

    while True:
        user = input("\nYour move: ").strip().lower()
        # ===== Additional Activity: Unknown handler ======
        if user not in VALID_MOVES and user != "exit":
            print("I didin't understand that, try again! (rock/paper/scissors/exit)")
            continue
        # ===== End Additional Activity =====

        if user == "exit":
            break

        predicted_user, conf = predict_next_move(freqs)
        comp = counter_move(predicted_user)
        result = winner(user, comp)

        freqs[user] += 1
        rounds += 1
        if result == 'win':
            stats["wins"] += 1
        elif result == "lose":
            stats["losses"] += 1
        else:
            stats["ties"] += 1
        
        print(f"AI predicted: {predicted_user} -> Computer played: {comp}")
        print(f"Round result: You {result}!")

        # Final report
        print("\n=== Final report (Part 2) ===")
        print(f"Rounds played: {rounds}")
        print(f"Wins: {stats['wins']} | Losses: {stats['losses']} | Ties: {stats['ties']}")
    if rounds > 0:
        win_rate = (stats['wins'] / rounds) * 100
        print(f"Win Rate: {win_rate:.1f}%")
        most = max(freqs, key=freqs.get)
        print(f"Your most frequent move was: {most} ({freqs[most]} times)")
        print(f"Next time the AI will counter with: {counter_move(most)}")


if __name__ == "__main__":
    play()