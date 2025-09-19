# Mission: Rotate list n positions without extra space

def rotate_list(lst, n):
    n = n % len(lst)  # handle rotations > length
    return lst[-n:] + lst[:-n]

def main():
    data = [1, 2, 3, 4, 5]
    n = 2
    rotated = rotate_list(data, n)
    print(f"List rotated by {n} positions:", rotated)

if __name__ == "__main__":
    main()
