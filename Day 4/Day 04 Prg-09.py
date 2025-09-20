# Armstrong number checker
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    return sum(int(d)**power for d in digits) == num

num = int(input("Enter a number: "))
print("Armstrong number" if is_armstrong(num) else "Not an Armstrong number")
