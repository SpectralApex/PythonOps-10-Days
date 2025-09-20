# Temperature converter between Celsius and Fahrenheit
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

choice = input("Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? ").upper()
temp = float(input("Enter temperature: "))

if choice == 'C':
    print(f"{temp}°C = {c_to_f(temp):.2f}°F")
elif choice == 'F':
    print(f"{temp}°F = {f_to_c(temp):.2f}°C")
else:
    print("Invalid choice")
