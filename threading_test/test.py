import threading
import time

num = 0


def add():
    global num
    for i in range(100_000):
        num += 1


def sub():
    global num
    for i in range(100_000):
        num -= 1


if __name__ == "__main__":
    for i in range(100):
        t1 = threading.Thread(target=add)
        t2 = threading.Thread(target=sub)
        t1.start()
        t2.start()

    # subThread01 = threading.Thread(target=add)
    # subThread02 = threading.Thread(target=sub)
    #
    # subThread01.start()
    # subThread02.start()
    #
    # subThread01.join()
    # subThread02.join()

    print("num result : %s" % num)
