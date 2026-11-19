import sys


def is_contained(c: str, characters: frozenset[str]) -> bool:
    """Return whether a character is contained in the given set."""
    return c in characters


def count_chars(text: str) -> dict[str, int]:
    """Count uppercase, lowercase, punctuation, spaces, and digits."""
    ascii_punctuation = frozenset(
        r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    )
    return {
        "total": len(text),
        "upper": sum(c.isupper() for c in text),
        "lower": sum(c.islower() for c in text),
        "punctuation": sum(
            is_contained(c, ascii_punctuation) for c in text
        ),
        "spaces": sum(c.isspace() for c in text),
        "digits": sum(c.isdigit() for c in text),
    }


def print_results(counts: dict[str, int]) -> None:
    """Print character counts in the required output format."""
    print(f"The text contains {counts['total']} characters:")
    for key, label in (
        ("upper", "upper letters"),
        ("lower", "lower letters"),
        ("punctuation", "punctuation marks"),
        ("spaces", "spaces"),
        ("digits", "digits"),
    ):
        print(f"{counts[key]} {label}")


def main():
    """Read the input text and print its character counts."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        text = sys.argv[1] if len(sys.argv) == 2 else ""
        if not text:
            print("What is the text to count?")
            text = open(0).readline()
        print_results(count_chars(text))
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1
    except KeyboardInterrupt:
        print("")
        return 130

    return 0


if __name__ == "__main__":
    main()
