#lcm and gcd of two numbers
import math

def gcd_lcm(a, b):
    gcd_val = math.gcd(a, b)
    lcm_val = abs(a * b) // gcd_val
    return gcd_val, lcm_val

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd_val, lcm_val = gcd_lcm(a, b)
print(f"GCD: {gcd_val}, LCM: {lcm_val}")
