
# Mission: Store and print first 100 natural numbers in ascending & descending order

def main():
    numbers = list(range(1, 100))  # Populate list with first 20 natural numbers
    print("Ascending order:", numbers)
    print("Descending order:", numbers[::-1])

if __name__ == "__main__":
    main()


