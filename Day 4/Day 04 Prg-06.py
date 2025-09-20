# Palindrome checker
def is_palindrome(s):
    s = str(s)
    return s == s[::-1]

word = input("Enter word or number: ")
print("Palindrome" if is_palindrome(word) else "Not a palindrome")
