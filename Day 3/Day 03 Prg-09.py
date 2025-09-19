# Mission: Find second largest number without sorting

def second_largest(lst):
    largest = second = float('-inf')
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num
    return second

def main():
    data = [10, 20, 4, 45, 99]
    result = second_largest(data)
    print("Second largest number:", result)

if __name__ == "__main__":
    main()
