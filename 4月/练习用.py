
import random
m = random.randint(1, 100)
count = 0
while True:
    n = int(input('请猜一个数字：'))
    if n < m:
        print('猜小了！')
    elif n > m:
        print('猜大了！')
    else:
        print('猜对了！')
        break

    count +=1
    if count >= 5:
        print('你猜了5次，游戏结束')
        break