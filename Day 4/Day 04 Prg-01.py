# Function to extract even digits from a number
def even_digit_extractor(num):
    evens = [d for d in str(num) if int(d) % 2 == 0]
    return ''.join(evens) if evens else "No even digits"

# Example
number = int(input("Enter a number: "))
print("Even digits:", even_digit_extractor(number))
