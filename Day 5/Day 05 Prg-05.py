# rock_paper_scissors.py
import random

CHOICES = ["rock", "paper", "scissors"]

def winner(player, computer):
    if player == computer:
        return "draw"
    wins = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }
    return "player" if wins[player] == computer else "computer"

def main():
    print("Rock, Paper, Scissors! Type 'quit' to stop.")
    while True:
        player = input("Your choice (rock/paper/scissors): ").strip().lower()
        if player == "quit":
            print("Goodbye!")
            break
        if player not in CHOICES:
            print("Invalid choice.")
            continue
        computer = random.choice(CHOICES)
        print(f"Computer chose: {computer}")
        result = winner(player, computer)
        if result == "draw":
            print("It's a draw.\n")
        elif result == "player":
            print("You win!\n")
        else:
            print("You lose.\n")

if __name__ == "__main__":
    main()
