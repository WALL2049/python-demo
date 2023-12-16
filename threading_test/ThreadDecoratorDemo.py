# coding=utf-8

import threading
import time


def thread_decorator(fun):
    def wrapper(*args):
        t1 = threading.Thread(target=fun, args=args)
        t1.start()
        t1.join()
        # threading.daemon = True  # 至于t1.setDaemon(True)，该写法已废弃，现在用：

    return wrapper


@thread_decorator
def withdraw_money(name, num):
    global money
    # lock.acquire()
    for i in range(num):
        money -= 1
        print(f"{name}取钱，取了{i + 1}次！")
        time.sleep(0.2)
    # lock.release()


@thread_decorator
def save_money(name, num):
    global money
    for i in range(num):
        money += 1
        print(f"{name}存钱，取了{i + 1}次！")


if __name__ == "__main__":
    print("===========START===========")
    money = 30000000
    lock = threading.Lock()
    withdraw_money("A", 10)
    save_money("B", 10)
    print(f"还剩{money}元")
    print("===========END===========")


# 如上，可以使用decorator装饰子线程，这样比thread_it函数更方便。
# 在UI界面时，子线程应当设置守护线程threading.daemon = True,已废弃Thread.setDaemon(true)，
# 方便主线程关闭时，子线程同步关闭，否则就后台运行了。
# 当需要子线程运行结束了再主线程时，加t1.join()。
# 当多个线程使用同一个资源变量，容易引起冲突时，加threading,Lock(),lock.acquire(),lock..release()



