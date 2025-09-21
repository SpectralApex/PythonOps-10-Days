# password_generator.py
import random
import string

def generate(length=12, use_upper=True, use_digits=True, use_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    symbols = "!@#$%^&*()-_=+[]{};:,.?/"

    pool = lower + upper + digits + (symbols if use_symbols else "")
    if not pool:
        raise ValueError("Character pool is empty.")

    # Ensure at least one from each selected category
    password_chars = []
    password_chars.append(random.choice(lower))
    if use_upper: password_chars.append(random.choice(upper))
    if use_digits: password_chars.append(random.choice(digits))
    if use_symbols: password_chars.append(random.choice(symbols))

    while len(password_chars) < length:
        password_chars.append(random.choice(pool))

    random.shuffle(password_chars)
    return "".join(password_chars[:length])

def main():
    print("Password Generator")
    try:
        length = int(input("Length (e.g., 12): "))
        use_upper = input("Include uppercase? (y/n): ").strip().lower() == "y"
        use_digits = input("Include digits? (y/n): ").strip().lower() == "y"
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"
        print("Generated password:", generate(length, use_upper, use_digits, use_symbols))
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
