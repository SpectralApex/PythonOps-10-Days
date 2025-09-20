# Character frequency in a string
def char_frequency(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

text = input("Enter a string: ")
for char, count in char_frequency(text).items():
    print(f"'{char}': {count}")
