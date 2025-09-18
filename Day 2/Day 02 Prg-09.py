# 9. Age Category Classifier
age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
elif age < 60:
    print("Adult")
else:
    print("Senior")
