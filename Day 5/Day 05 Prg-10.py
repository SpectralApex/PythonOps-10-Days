# random_joke.py
import random

JOKES = {
    "general": [
        "Why don’t scientists trust atoms? Because they make up everything.",
        "I told my computer I needed a break, and it said 'No problem — I’ll go to sleep.'",
        "Why did the scarecrow get promoted? He was outstanding in his field.",
    ],
    "programming": [
        "There are 10 kinds of people: those who understand binary and those who don’t.",
        "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
        "I would tell you a UDP joke, but you might not get it.",
    ],
    "dad": [
        "I’m reading a book on anti-gravity. It’s impossible to put down.",
        "What do you call fake spaghetti? An impasta.",
        "I used to hate facial hair, but then it grew on me.",
    ],
}

def get_joke(category=None):
    if category and category in JOKES:
        return random.choice(JOKES[category])
    all_jokes = [j for jokes in JOKES.values() for j in jokes]
    return random.choice(all_jokes)

def main():
    print("Random Joke Generator")
    print("Categories:", ", ".join(JOKES.keys()))
    cat = input("Choose a category (or press Enter for any): ").strip().lower()
    cat = cat if cat in JOKES else None
    print("\nHere's a joke:")
    print(get_joke(cat))

if __name__ == "__main__":
    main()
