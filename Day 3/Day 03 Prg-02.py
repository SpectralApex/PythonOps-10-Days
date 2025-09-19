# Mission: Find largest and smallest number without max()/min()

def find_min_max(lst):
    if not lst:
        return None, None
    min_val = lst[0]
    max_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

def main():
    data = [5, 2, 9, 1, 7, 3]  # Example list
    smallest, largest = find_min_max(data)
    print("Smallest number:", smallest)
    print("Largest number:", largest)

if __name__ == "__main__":
    main()