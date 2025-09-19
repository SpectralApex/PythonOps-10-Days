# Mission: Squares of even numbers from 1 to 50

def main():
    squares = [x**2 for x in range(1, 51) if x % 2 == 0]
    print("Squares of even numbers 1–50:", squares)

if __name__ == "__main__":
    main()
