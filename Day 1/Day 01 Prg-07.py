import random

n = int(input("How many times do you want to flip the coin? "))

for i in range(1, n + 1):
    result = random.choice(["Heads", "Tails"])
    print("Flip", i, ":", result)