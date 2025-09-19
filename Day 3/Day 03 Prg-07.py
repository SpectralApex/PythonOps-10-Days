# Mission: Unpack tuple of coordinates

def main():
    coords = (10, 20, 30)
    x, y, z = coords
    print(f"x: {x}, y: {y}, z: {z}")
    print("Sum of coordinates:", x + y + z)

if __name__ == "__main__":
    main()
