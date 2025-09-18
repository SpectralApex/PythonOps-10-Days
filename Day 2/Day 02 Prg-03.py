# 3. Leap Year Checker
n = int(input("how many years you want to check? "))
total = 0
for i in range(1, n + 1):
    year = int(input("Enter a year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")


