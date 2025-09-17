user_input = input("Enter a number for its multiplication table (or press Enter for all): ")

if user_input.strip() == "":
    print("Multiplication Table 1 to 10")
    for row in range(1, 11):
        for col in range(1, 11):
            print(row * col, end="\t")
        print()
else:
    number = int(user_input)
    print(f"Multiplication Table for {number}")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")