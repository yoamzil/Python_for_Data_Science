import sys


def countChar(string):
    """Counts upper, lower, punctuation, space, and digit characters"""
    total = len(string)
    upper = 0
    lower = 0
    punctuation = 0
    space = 0
    digit = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            space += 1
        else:
            punctuation += 1

    print(
        f"The text contains {total} characters:\n\
{upper} upper letters\n\
{lower} lower letters\n\
{punctuation} punctuation marks\n\
{space} spaces\n\
{digit} digits"
    )


def main(argv):
    """tests and error handling"""
    try:
        if len(argv) > 2:
            raise AssertionError("AssertionError: too many arguments")
        if len(argv) == 1:
            print("What is the text to count?")
            text = sys.stdin.read()
            countChar(text)
        else:
            countChar(argv[1])
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main(sys.argv)
