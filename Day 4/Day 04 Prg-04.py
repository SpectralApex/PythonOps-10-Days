# Factorial using iteration and recursion
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    return 1 if n <= 1 else n * factorial_recursive(n - 1)

n = int(input("Enter a number: "))
print("Iterative:", factorial_iterative(n))
print("Recursive:", factorial_recursive(n))
