def count_in_list(lst, value):
    """Counts the number of occurrences of a value in a list"""
    return lst.count(value)


def main():
    """tests and error handling"""
    print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
    print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 0


if __name__ == "__main__":
    main()
