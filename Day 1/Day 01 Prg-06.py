n = int(input("how many times you want to pick a random number?:"))
for i in range(n):
    numbers = range(1, n + 1)
    import random
    picked_number = random.choice(numbers)
    if picked_number <=10:
        print(f"Here is your number Hurayyyyyyyyyyyyyyyy:{picked_number}")
    else:
        pass




