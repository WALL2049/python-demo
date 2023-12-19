# coding=utf-8

import time


def quickSortList(alist):
    if len(alist) >= 2:
        base = alist[0]
        left = []
        right = []
        alist.remove(base)
        for i in alist:
            if i < base:
                left.append(i)
            else:
                right.append(i)

        return quickSortList(left) + [base] + quickSortList(right)
    else:
        return alist






def quickSortIndex(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

    return alist


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotpoint = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotpoint:
            leftmark += 1
        while leftmark <= rightmark and alist[rightmark] >= pivotpoint:
            rightmark -= 1
        if leftmark > rightmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    alist[first] = alist[rightmark]
    alist[rightmark] = pivotpoint

    return rightmark




if __name__ == '__main__':
    start = time.time()
    alist = [4, 84, 3, 7, 38, 19, 12, 97, 88, 53, 42, 73, 10, 46, 4, 29, 73]
    print(quickSortList(alist))
    end = time.time()
    print(end - start)
