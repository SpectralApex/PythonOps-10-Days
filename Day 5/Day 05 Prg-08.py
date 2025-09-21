# hangman.py
import random
import string

WORDS = [
    "python", "hangman", "kerala", "monsoon", "coconut",
    "developer", "algorithm", "coffee", "laptop", "ocean"
]

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong = 0
    max_wrong = len(HANGMAN_PICS) - 1
    print("Welcome to Hangman!")
    while True:
        print(HANGMAN_PICS[wrong])
        display = " ".join([c if c in guessed else "_" for c in word])
        print("Word:", display)
        print("Guessed:", " ".join(sorted(guessed)) or "-")
        if "_" not in display.replace(" ", ""):
            print("You guessed it! The word was:", word)
            break
        if wrong >= max_wrong:
            print("You lost. The word was:", word)
            break
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Enter a single alphabetic character.\n")
            continue
        if guess in guessed:
            print("You already guessed that.\n")
            continue
        guessed.add(guess)
        if guess not in word:
            wrong += 1
            print("Wrong guess!\n")
        else:
            print("Good guess!\n")

if __name__ == "__main__":
    play()
