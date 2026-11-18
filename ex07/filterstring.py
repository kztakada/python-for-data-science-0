import sys


def main():
    """Print the words of S that are longer than N."""
    try:
        assert len(sys.argv) == 3
        s = sys.argv[1]
        n_arg = sys.argv[2]
        assert isinstance(s, str)
        assert isinstance(n_arg, str)
        digits = n_arg[1:] if n_arg[:1] in ("+", "-") else n_arg
        assert digits and all("0" <= digit <= "9" for digit in digits)
        n = int(n_arg)
        is_longer = lambda word: len(word) > n
        print([word for word in filter(is_longer, s.split())])
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")
        return 1

    return 0


if __name__ == "__main__":
    main()
