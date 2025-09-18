# 5. Temperature Alert
temp = float(input("Enter temperature in °C: "))

if temp < 15:
    print("Cold")
elif temp <= 30:
    print("Warm")
else:
    print("Hot")
