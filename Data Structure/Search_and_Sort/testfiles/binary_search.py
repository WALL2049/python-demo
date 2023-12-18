class BinarySearch:
    def __init__(self):
        pass

    @staticmethod
    def binary_search(alist, item):
        while True:
            if len(alist) == 0:
                return False
            index = len(alist) // 2
            if alist[index] > item:
                alist = alist[:index]
            elif alist[index] < item:
                alist = alist[index + 1:]
            elif alist[index] == item:
                return True

    @staticmethod
    def binary_search_recursion(alist, item):
        if len(alist) == 0:
            return False
        index = len(alist) // 2
        if alist[index] > item:
            return BinarySearch.binary_search_recursion(alist[:index], item)
        if alist[index] < item:
            return BinarySearch.binary_search_recursion(alist[index + 1:], item)
        if alist[index] == item:
            return True


if __name__ == "__main__":
    alist = [i for i in range(10)]
    print(BinarySearch.binary_search(alist, 11))
    print(BinarySearch.binary_search_recursion(alist, 8))
