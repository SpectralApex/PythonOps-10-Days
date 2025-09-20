# Simple Interest Calculator
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate (%): "))
t = float(input("Enter time (years): "))
print("Simple Interest:", simple_interest(p, r, t))
