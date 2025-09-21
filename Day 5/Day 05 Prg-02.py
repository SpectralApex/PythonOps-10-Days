# tip_calculator.py
# Calculate tip and split bill

def tip_calculator():
    print("Tip Calculator")
    while True:
        try:
            bill = float(input("Bill amount: "))
            if bill < 0: raise ValueError
            break
        except ValueError:
            print("Enter a valid non-negative number.")
    while True:
        try:
            tip_percent = float(input("Tip percentage (e.g., 10, 12.5, 15): "))
            if tip_percent < 0: raise ValueError
            break
        except ValueError:
            print("Enter a valid non-negative number.")
    while True:
        try:
            people = int(input("Number of people splitting the bill: "))
            if people <= 0: raise ValueError
            break
        except ValueError:
            print("Enter a positive whole number.")
    tip_amount = bill * (tip_percent / 100)
    total = bill + tip_amount
    per_person = total / people
    print(f"\nTip amount: ₹{tip_amount:.2f}")
    print(f"Total bill: ₹{total:.2f}")
    print(f"Each person pays: ₹{per_person:.2f}")

if __name__ == "__main__":
    tip_calculator()
