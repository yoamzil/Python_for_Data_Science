import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """returns a list of BMI values"""
    if len(height) != len(weight):
        raise ValueError("lists must be the same size")
    if not all(isinstance(x, (int, float)) for x in height):
        raise ValueError("height and weight must be lists of int or float")
    if not all(isinstance(x, (int, float)) for x in weight):
        raise ValueError("height and weight must be lists of int or float")

    h = np.array(height)
    w = np.array(weight)
    return (w / h**2).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """returns a list of bool indicating whether the BMI is above the limit"""
    if not all(isinstance(x, (int, float)) for x in bmi):
        raise ValueError("bmi must be a list of int or float")
    if not isinstance(limit, int):
        raise TypeError("limit must be an int")
    return (np.array(bmi) > limit).tolist()


def main():
    """tests and error handling"""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    try:
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except (ValueError, TypeError) as e:
        print(e)


if __name__ == "__main__":
    main()
