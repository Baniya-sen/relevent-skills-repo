def main():
    """If user input is not between 1 and 8 inclusive, then ask repeatedly"""
    while True:
        try:
            height = int(input("Height: "))
            if height > 0 and height < 9:
                break
        except ValueError:
            pass

    print_pyramid(height)


def print_pyramid(height):
    """Print two pyramids of half same height"""
    for i in range(0, height):
        print(" " * (height - (i + 1)), end="")
        print("#" * (i + 1), end="")
        print("  ", end="")
        print("#" * (i + 1))


if __name__ == "__main__":
    main()
    