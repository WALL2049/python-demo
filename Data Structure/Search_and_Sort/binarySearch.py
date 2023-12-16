# coding = utf-8
import time

def binaryListSearch(list, item):
    found = False
    while not found:
        pos = len(list) // 2
        if list[pos] > item:
            list = list[0:pos-1]
        elif list[pos] < item:
            list = list[pos+1:len(list)]
        elif list[pos] == item:
            found = True

    return found

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

def binaryIndexRecursionSearch(list, item):
    first = 0
    last = len(list) - 1
    if len(list) == 0:
        return False
    else:
        midpoint = (first + last) // 2
        if list[midpoint] == item:
            return True
        elif list[midpoint] < item:
            return binaryIndexRecursionSearch(list[midpoint + 1:], item)
        elif list[midpoint] > item:
            return binaryIndexRecursionSearch(list[:midpoint - 1], item)

    return found



if __name__ == "__main__":
    start = time.time()
    list = [i for i in range(10000000)]
    result = binaryListSearch(list, 5 ^ 8)
    end = time.time()
    print(result)
    print(end - start)

    start = time.time()
    list = [i for i in range(10000000)]
    result = binaryIndexSearch(list, 5 ^ 8)
    end = time.time()
    print(result)
    print(end - start)

    start = time.time()
    list = [i for i in range(10000000)]
    result = binaryIndexRecursionSearch(list, 5 ^ 8)
    end = time.time()
    print(result)
    print(end - start)









