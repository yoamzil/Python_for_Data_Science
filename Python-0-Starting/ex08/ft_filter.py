def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true. """
    if function is None:
        for item in iterable:
            if item:
                yield item
    else:
        for item in iterable:
            if function(item):
                yield item


def main():
    """tests"""

    print(list(ft_filter(lambda x: x % 2 == 0, range(10))))
    print(list(ft_filter(None, [0, 1, False, 2, "", "hello"])))


if __name__ == "__main__":
    main()
