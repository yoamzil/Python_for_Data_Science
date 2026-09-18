import sys


def turnToMorse(string, nested_morse):
    """takes a string an encodes into Morse Code"""
    try:
        length = len(string)
        for char in string:
            if char.upper() not in nested_morse:
                raise AssertionError("AssertionError: the arguments are bad")
        for index, char in enumerate(string):
            if index == length - 1:
                print(nested_morse[char.upper()], end="")
            else:
                print(nested_morse[char.upper()], end=" ")
        print()
    except AssertionError as e:
        print(e)
        sys.exit(1)


def main(argv):
    """tests and error handling"""
    try:
        NESTED_MORSE = {
            " ": "/",
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
        }
        if len(argv) != 2:
            raise AssertionError("AssertionError: the arguments are bad")
        turnToMorse(argv[1], NESTED_MORSE)
    except AssertionError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)
