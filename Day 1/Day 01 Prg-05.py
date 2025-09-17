n = int(input("How many numbers do you want to enter? "))
sum = 0

for i in range(1, n + 1):
    number = float(input("Enter number " + str(i) + ": "))
    sum = sum + number

average = sum / n

print("Sum =", sum)
print("Average =", average) 