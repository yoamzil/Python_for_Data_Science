import sys


def check_num(num):
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main(argv):
    if len(argv) < 2:
        sys.exit(0)
    try:
        assert len(argv) <= 2, "AssertionError: more than one argument is provided"
        num = int(argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit(1)
    except AssertionError as e:
        print(e)
        sys.exit(1)

    check_num(num)


if __name__ == "__main__":
    main(sys.argv)
