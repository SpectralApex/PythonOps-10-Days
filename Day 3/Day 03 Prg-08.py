# Mission: Split list into even and odd numbers

def split_even_odd(lst):
    evens = []
    odds = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return evens, odds

def main():
    data = [1, 2, 3, 4, 5, 6]
    evens, odds = split_even_odd(data)
    print("Even numbers:", evens)
    print("Odd numbers:", odds)

if __name__ == "__main__":
    main()
