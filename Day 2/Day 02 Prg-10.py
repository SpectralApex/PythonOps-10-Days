# 10. Password Strength Checker
password = input("Enter password: ")

if len(password) < 6:
    print("Weak")
elif len(password) < 10:
    print("Medium")
else:
    print("Strong")
# Additional checks for character types
has_upper = any(c.isupper() for c in password)
