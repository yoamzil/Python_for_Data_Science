from typing import Any


def all_thing_is_obj(object: Any) -> int:
    try:
        if isinstance(object, list):
            print("List : " + str(type(object)))
        elif isinstance(object, tuple):
            print("Tuple : " + str(type(object)))
        elif isinstance(object, set):
            print("Set : " + str(type(object)))
        elif isinstance(object, dict):
            print("Dict : " + str(type(object)))
        else:
            print(object + " is in the kitchen : " + str(type(object)))
    except TypeError:
        print("Type not found")
    return 42
