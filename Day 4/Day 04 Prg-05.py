# Fibonacci sequence generator
def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

n = int(input("Enter number of terms: "))
print("Fibonacci sequence:", fibonacci(n))
