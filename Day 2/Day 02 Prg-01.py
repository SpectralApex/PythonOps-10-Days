# 1. Grade Evaluator for Multiple Marks and Average

n = int(input("Enter how many subjects you want to enter? "))
total = 0

for i in range(1, n + 1):
    marks = int(input("Enter marks: "))
    total += marks

    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 40:
        print("Grade: D")
    else:
        print("Grade: F")

average = total / n
print("Average marks:", average)

if average >= 90:
    print("Grade for average: A")
elif average >= 75:
    print("Grade for average: B")
elif average >= 60:
    print("Grade for average: C")
elif average >= 40:
    print("Grade for average: D")
else:
    print("Grade for average: F")