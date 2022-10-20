# coding=utf-8

import time

#dp   dynamic programming, minCoins是存储用来每一步的硬币数的列表, coinsUsed记录每一步使用的硬币
def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    #从1开始到change逐个计算最少硬币数
    for totalnum in range(1, change + 1):
        coinsCount = totalnum   #最大数
        newcoin = 1     #记录每次使用的硬币币值
        for i in [j for j in coinValueList if j <= change and (totalnum - j) >= 0]:
            if minCoins[totalnum - i] + 1 < coinsCount:
                coinsCount = minCoins[totalnum - i] + 1
                newcoin = i
        coinsUsed[totalnum] = newcoin
        minCoins[totalnum] = coinsCount

    return minCoins[change]

    # print(f'每一总数所需要的最少硬币数列表为{minCoins}')
    # print(f'每一步选择的硬币为{coinsUsed}')


if __name__ == '__main__':
    a = time.time()
    result = dpMakeChange([1, 5, 10, 21, 25], 63, [0]*64, [0]*64)
    print(result)
    b = time.time()
    print(b-a)


    # for i in range(1, 10):
    #     print(i)