# coding=utf-8

'''
如果函数没有入参，那么直接def thread_it(func)即可，没有问题
如果有入参，如果使用thread_it(Key('Chrome', 'headless'))这种做法，是没有起多线程的，入参必须写在后面args里
如果一个入参，这样就可以：(多个入参其实也一样，这里本就是个元祖入参，不用考虑*args)
@staticmethod
    def thread_it(func, args):
        t = threading.Thread(target=func, args=args)
        t.start()
        # t.setDaemon(True)
        # t.join()

if __name__ == "__main__":
    def count_num(name):
        for i in range(10):
            print(f"计数{name}, 第{i}次\t---")
            time.sleep(0.3)
    t1 = ThreadDemo1()
    t1.thread_it(count_num, ("A"))
    # count_num("A")
    count_num("B")
    count_num("C")
    print("OVER!!!!!!")
'''
import threading
import time


class ThreadDemo1:
    def __init__(self):
        pass

    @staticmethod
    def thread_it(func, args):
        t = threading.Thread(target=func, args=args)
        t.start()
        # t.setDaemon(True)
        # t.join()


if __name__ == "__main__":
    lock = threading.Lock()


    def count_num(name, num):
        lock.acquire()
        for i in range(num):
            print(f"计数{name}, 第{i}次\t---")
            time.sleep(0.2)
        lock.release()


    t1 = ThreadDemo1()

    t1.thread_it(count_num, ("A", 10))
    t1.thread_it(count_num, ("B", 12))
    # t1.thread_it(count_num, ("C", 8))
    print("OVER!!!!!!")
