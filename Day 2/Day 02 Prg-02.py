# 2. Age to 30 Calculator

def years_until_30():
    name = input("Enter your name: ").strip()

    while True:
        age_input = input("Enter your age: ").strip()
        if age_input.isdigit():
            age = int(age_input)
            break
        else:
            print("❌ Please enter a valid number for age.")

    if age < 30:
        years_left = 30 - age
        print(f"Hello {name}, you will be 30 years old in {years_left} year{'s' if years_left > 1 else ''}.")
    elif age == 30:
        print(f"Hello {name}, you are already 30 years old! 🎉")
    else:
        years_over = age - 30
        print(f"Hello {name}, you turned 30 {years_over} year{'s' if years_over > 1 else ''} ago.")

years_until_30()