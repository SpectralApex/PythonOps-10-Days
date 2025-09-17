import random
print(" Welcome to the Dice Rolling Challenge!")
target_score = 20
score = 0

while score < target_score:
    input("Press Enter to roll the dice...!")
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}!")
    score += roll
    print(f"Your total score is now {score}\n")

print(" Congratulations! You reached the target score!")
