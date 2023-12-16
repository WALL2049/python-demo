a = 1
l = [1, 2, 3]


def test1():
    global a  #不可变类型需要声明全局变量
    a += 1
    print(a)


def test2():
    print(a)


def test3():
    l.append(4)  #可变类型可直接调用全局变量
    print(l)


def test4():
    print(l)


test1()
test2()
test3()
test4()
print(a)
print(type(a))
print(l)
print(type(l))


name1 = ('kevin')
abc = 'qwer1234'
name2 = 'kevin'
name3 = name1
name4 = name1.copy()


