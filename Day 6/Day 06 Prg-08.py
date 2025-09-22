# Flashcard Quiz
cards = {"Python": "A programming language", "RAM": "Temporary memory", "Loop": "Repeats code"}

for term, definition in cards.items():
    ans = input(f"What is {term}? ")
    print("✅" if ans.lower() == definition.lower() else f"❌ Correct: {definition}")
