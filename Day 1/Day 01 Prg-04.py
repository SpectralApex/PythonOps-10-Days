
number = int(input("Enter a number between 1 and 50: "))

if number < 1 or number > 50:
    print("Please enter a number between 1 and 50.")
else:
    if number % 2 == 0:
        print(number, "is EVEN")
    else:
        print(number, "is ODD")