# Mission: Remove duplicates while preserving order

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def main():
    data = [1, 2, 2, 3, 4, 4, 5]
    result = remove_duplicates(data)
    print("Without duplicates:", result)

if __name__ == "__main__":
    main()
