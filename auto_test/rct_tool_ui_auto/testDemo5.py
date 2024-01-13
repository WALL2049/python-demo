# for i in range(1, 30 , 2):
#     print(i, end=' ')
# print()
# alist = [1,2,3,4]
# print(len(alist))
#


class TestDemo:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

if __name__ == "__main__":
    t1 = TestDemo(10)
    # print(t1._value)
    print(t1.value)
    # t1._value = 20
    print(t1.value)
    t1.value = 30
    print(t1.value)

