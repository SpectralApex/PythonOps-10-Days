# Mission: Count frequency of each element

def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

def main():
    data = [1, 2, 2, 3, 3, 3, 4]
    frequency = count_frequency(data)
    print("Frequencies:", frequency)

if __name__ == "__main__":
    main()
