# Floyd's Triangle
def floyds_triangle(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

rows = int(input("Enter number of rows: "))
floyds_triangle(rows)
