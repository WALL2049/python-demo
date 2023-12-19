class Search:
    def __init__(self):
        pass

    @staticmethod
    def search_list(alist, item):
        for index in range(len(alist)):
            if alist[index] != item:
                continue
            else:
                return index


if __name__ == "__main__":
    alist = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    result = Search.search_list(alist, 7)
    print(result)



