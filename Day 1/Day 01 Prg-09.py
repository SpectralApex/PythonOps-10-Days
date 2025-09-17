import random

print(" Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 100)
guess = None
attempts = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.\n")
    elif guess > secret_number:
        print("Too high! Try again.\n")
    else:
        print(f" Correct! The number was {secret_number}.")
        print(f"You guessed it in {attempts} attempts.")
