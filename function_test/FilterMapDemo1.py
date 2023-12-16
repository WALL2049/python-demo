class FilterMapDemo1:
    def __init__(self):
        pass


if __name__ == "__main__":
    list1 = [0, 1, 2, 3, 4, 5, 6]
    result1 = list(filter(lambda x: x > 3, list1))
    print(result1)

    result2 = list(map(lambda x: x**2, list1))
    print(result2)

