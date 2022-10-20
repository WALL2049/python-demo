# coding = utf-8
import time

def sequentialSearch(list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(list) and not found and not stop:
        if list[pos] <= item:
            if list[pos] != item:
                pos += 1
            else:
                found = True
        else:
            stop = True

    return found


if __name__ == "__main__":
    start = time.time()
    list = [i for i in range(100000000)]
    result = sequentialSearch(list, 5^11)
    end = time.time()
    print(result)
    print(end - start)
