import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D array along the first axis.
    Returns:
        list: The sliced array as a list.
    """
    arr = np.array(family)
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    if arr.ndim != 2:
        raise ValueError("family must be a 2D array")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")
    print(f"My shape is : {arr.shape}")
    sliced = arr[start:end]
    print(f"My new shape is : {sliced.shape}")
    return sliced.tolist()


def main():
    """tests and error handling"""
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
