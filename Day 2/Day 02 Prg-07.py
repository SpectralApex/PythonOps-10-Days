# 7. Discount Calculator
amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = 0.20
elif amount >= 2000:
    discount = 0.10
else:
    discount = 0.05

final_price = amount - (amount * discount)
print(f"Discount: {discount*100}%")
print(f"Final Price: {final_price}")
