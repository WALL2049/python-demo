# -*- coding: UTF-8 -*-

import time
import threading


class ThreadDemo0:
    def __init__(self):
        pass

    def test_fun(self, name):
        for i in range(5):
            print(name, i)
            time.sleep(0.5)


if __name__ == "__main__":

    t = ThreadDemo0()
    t1 = threading.Thread(target=t.test_fun, args=("计数A",))
    t1.start()
    t1.join()
    t2 = threading.Thread(target=t.test_fun, args=("计数B",))
    t2.start()
    t3 = threading.Thread(target=t.test_fun, args=("计数C",))
    t3.start()
    print("完成！")

    # target 参数 指定 新线程要执行的函数
    # 注意，这里指定的函数对象只能写一个名字，不能后面加括号，
    # 如果加括号就是直接在当前线程调用执行，而不是在新线程中执行了

    # 如果 新线程函数需要参数，在 args里面填入参数
    # 注意参数是元组， 如果只有一个参数，后面要有逗号，像这样 args=('参数1',)
