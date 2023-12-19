# coding = utf-8

import time

def selectionSort(alist):
    locationOfMax = 0
    for sortnum in range(len(alist)-1, 0, -1):
        for location in range(0, sortnum+1):
            if alist[location] > alist[locationOfMax]:
                locationOfMax = location
        temp = alist[locationOfMax]
        alist[locationOfMax] = alist[sortnum]
        alist[sortnum] = temp
    return alist


if __name__ == '__main__':
    start = time.time()
    alist = [55,256,84,3,7,4,86,9,43,788,4,425,667,34,73]
    print(selectionSort(alist))
    end = time.time()
    print(end - start)