# coding=utf-8
import time

def getMC(coinsValueList, change):      #coin列表，change次数也即minCoins次数
    minCoins = change
    if change in coinsValueList:
        return 1
    for c in [c for c in coinsValueList if c <= change]:
        numCoins = 1 + getMC(coinsValueList, change - c)
        if numCoins < minCoins:
            minCoins = numCoins
    return minCoins


if __name__ == '__main__':
    print(time.perf_counter())
    print(getMC([1,5,10,21,25], 63))
    print(time.perf_counter())                #花费30秒，迭代太多太慢了