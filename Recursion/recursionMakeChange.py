# coding=utf-8
import time

def recursionMakeChange(coinsValueList, change, knownResults):    #coin列表，change次数也即minCoins次数，另外加一个存储最优解次数的列表
    minCoins = change
    if change in coinsValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0 :
        return knownResults[change]
    for c in [c for c in coinsValueList if c <= change]:
        numCoins = 1 + recursionMakeChange(coinsValueList, change - c, knownResults)
        if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
    return minCoins


if __name__ == '__main__':
    print(time.perf_counter())
    print(recursionMakeChange([1, 5, 10, 25], 63, [0] * 64))
    print(time.perf_counter())