import math
from typing import Any


def NULL_not_found(object: Any) -> int:
    try:
        if object is None:
            print("Nothing: " + str(object) + " " + str(type(object)))
        elif type(object) is float and math.isnan(object):
            print("Cheese: " + str(object) + " " + str(type(object)))
        elif type(object) is bool and object is False:
            print("Fake: " + str(object) + " " + str(type(object)))
        elif type(object) is int and object == 0:
            print("Zero: " + str(object) + " " + str(type(object)))
        elif type(object) is str and object == "":
            print("Empty: " + str(object) + str(type(object)))
        elif type(object) is str:
            print("Type not found")
            return 1
        else:
            print("Type not found")
            return 1
    except TypeError:
        print("Type not found")
        return 1
    return 0
