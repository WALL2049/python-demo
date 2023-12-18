# coding = utf-8

import time


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
    return alist
    # passnum = len(alist) - 1                #上下两种循环方式是一样的
    # while passnum > 0:
    #     for i in range(passnum):
    #         if alist[i] > alist[i + 1]:
    #             temp = alist[i]
    #             alist[i] = alist[i + 1]
    #             alist[i + 1] = temp
    #     passnum -= 1
    # return alist


# 或者
# for i in range(len(alist)):
#     for j  in range(0, len(alist)-i-1):
#         后面一样交换
#         alist[j],alist[j+1]=alist[j+1],alist[j]


def shortBubbleSort(alist):
    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
                exchange = True
        passnum -= 1
    return alist


if __name__ == '__main__':
    start = time.time()
    alist = [55, 256, 84, 3, 7, 4, 86, 9, 43, 788, 4, 425, 667, 34, 73]
    print(bubbleSort(alist))
    end = time.time()
    print(end - start)

    a = [None] * 5
    print(a)
    print(type(a))
    print(a == None)
    print(a is None)
    print(a == [])
