# coding=utf-8
import time



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

# 下面这种方式，值如果比较大，计算时间过长
    @staticmethod
    def binaryIndexSearch(list, item):
        found = False
        first = 0
        last = len(list) - 1
        while not found:
            midpoint = (first + last) // 2
            if list[midpoint] == item:
                found = True
            if list[midpoint] < item:
                first = midpoint + 1
            if list[midpoint] > item:
                last = midpoint - 1

        return found


if __name__ == "__main__":
    start = time.time()
    list = [i for i in range(10000000)]
    result = BinarySearch.binary_search(list, 5**8)
    end = time.time()
    print(result)
    print(end - start)

    start = time.time()
    list = [i for i in range(10000000)]
    result = BinarySearch.binaryIndexSearch(list, 5**8)
    end = time.time()
    print(result)
    print(end - start)

    start = time.time()
    list = [i for i in range(10000000)]
    result = BinarySearch.binary_search_recursion(list, 5**8)
    end = time.time()
    print(result)
    print(end - start)









