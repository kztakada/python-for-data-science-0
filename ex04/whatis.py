import sys


def main() -> int:
    args = sys.argv[1:]

    if len(args) == 0:
        return 0
    if len(args) > 1:
        print("AssertionError: more than one argument is provided")
        return 1

    try:
        n = int(args[0])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return 1

    if n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
