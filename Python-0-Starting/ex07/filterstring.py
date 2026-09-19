import sys


def filterstring(string, number):
    """Filters words from a string that are longer than a given number."""
    words = string.split(" ")
    filtered_words = [word for word in words
                      if (lambda w: len(w) > number)(word)]
    print(filtered_words)


def main(argv):
    """tests and error handling"""
    try:
        if len(argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")
        number = int(argv[2])
        filterstring(argv[1], number)
    except ValueError:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    except AssertionError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)
