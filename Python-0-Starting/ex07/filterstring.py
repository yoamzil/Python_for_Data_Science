import sys


def filterstring(string, number):
    print("success")


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
