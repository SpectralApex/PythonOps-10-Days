# Dice Roll Simulation
import random

rolls = [random.randint(1, 6) for _ in range(100)]
for i in range(1, 7):
    print(f"{i}: {rolls.count(i)} times")
