correct_password = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter access code: ")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        attempts += 1
        print(f"Incorrect! {max_attempts-attempts} attempts left.")
else:
    print("Locked out. Too many failed attempts.")
    print("Try again tomorrow.")
