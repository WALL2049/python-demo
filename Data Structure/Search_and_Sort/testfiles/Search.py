class Search:
    def __init__(self):
        pass

    @staticmethod
    def search_list(alist, item):
        index = 0
        while index <= len(alist):
            for i in range(len(alist)):
                if alist[i] != item:
                    continue
                else:
                    return i


if __name__ == "__main__":
    alist = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    result = Search.search_list(alist, 7)
    print(result)
