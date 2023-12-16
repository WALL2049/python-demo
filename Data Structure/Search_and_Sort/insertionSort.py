# coding=utf-8
import time


def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position -1]              # 插入排序，交换1次，相比冒泡交换3次更优
            position -= 1
        alist[position] = currentvalue

    return alist


def insertionSort2(alist):
    for index in range(1, len(alist)):
        while index > 0 and alist[index - 1] > alist[index]:   #反向冒泡排序，并非插入排序
            temp = alist[index]
            alist[index] = alist[index -1]
            alist[index - 1] = temp
            index -= 1

    return alist


if __name__ == '__main__':
    start = time.time()
    alist = [55,256,84,3,7,4,86,9,43,788,4,425,667,34,73]
    print(insertionSort(alist))
    # alist.sort()
    # print(alist)
    end = time.time()
    print(end - start)