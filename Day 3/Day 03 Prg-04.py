# Mission: Merge two lists and sort without sort()

def custom_sort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def main():
    list1 = [5, 1, 9]
    list2 = [8, 3, 2]
    merged = list1 + list2
    sorted_list = custom_sort(merged)
    print("Sorted merged list:", sorted_list)

if __name__ == "__main__":
    main()
