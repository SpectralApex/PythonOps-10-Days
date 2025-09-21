# currency_converter.py
# Simple converter using static example rates relative to USD

RATES = {
    # Base: USD
    "USD": 1.0,
    "EUR": 0.92,
    "INR": 83.0,
    "GBP": 0.79,
    "JPY": 147.0,
    "AED": 3.67,
}

def convert(amount, from_code, to_code):
    if from_code not in RATES or to_code not in RATES:
        raise ValueError("Unsupported currency code.")
    usd = amount / RATES[from_code]
    return usd * RATES[to_code]

def main():
    print("Currency Converter (static demo rates, update RATES for new values)")
    print("Supported:", ", ".join(sorted(RATES.keys())))
    try:
        amount = float(input("Amount: "))
        from_code = input("From currency code (e.g., USD): ").strip().upper()
        to_code = input("To currency code (e.g., INR): ").strip().upper()
        result = convert(amount, from_code, to_code)
        print(f"{amount:.2f} {from_code} = {result:.2f} {to_code}")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
