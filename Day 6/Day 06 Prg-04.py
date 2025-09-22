# Cybersecurity Terms Dictionary
terms = {
    "phishing": "Tricking users into revealing sensitive info via fake emails or websites.",
    "firewall": "A security system that controls incoming/outgoing network traffic.",
    "hashing": "Converting data into a fixed-size string for integrity checks."
}

term = input("Enter cybersecurity term: ").lower()
print(terms.get(term, "Term not found."))
