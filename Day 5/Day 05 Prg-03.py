# mad_lib.py
# Fill-in-the-blanks story

def mad_lib():
    print("Let's create a story!")
    adj = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (past tense): ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    food = input("Enter a food: ")

    story = (
        f"On a {adj} morning in {place}, I found a {noun} that could talk. "
        f"It {verb} around like a {animal} on a trampoline. "
        f'We shared some {food} and agreed to keep each other\'s secrets.'
    )
    print("\nYour story:\n")
    print(story)

if __name__ == "__main__":
    mad_lib()
