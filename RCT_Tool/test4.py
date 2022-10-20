# while True:
#     a = input('请输入：')
#     try:
#         b = int(a)
#         assert b < 9999, '这次输入的值有些大，不对！'
#         c = 2
#         # if b > 9999:
#         #     raise NameError
#         print(b+c)
#     except NameError:
#         print('值太大了')
#     except ValueError as error:
#         print('输入的值有误')
#         print(error)

import copy
# x = 'xxx'
# y = 'yyy'
# q = 1
# w = 2
# a = {'k1':'v1', 'k2':{x:[q,w]}}
# b = copy.copy(a)
# a['k1'] = 123
# # a['k2'] = 456
# x = 999
# y = 888
# q = 4
# w = 5
# print(a)
# print(b)

# x = 'xxx'
# y = [1,2]
# q = 'qwer'
# w = [7,8]
# a = (x,y,[q,w])
# b = copy.copy(a)
# x = 'consist'
# y.append(3)
# q = 'apple'
# w.remove(7)
# print(a)
# print(b)

# s='python'
# print(s.index('h'))

# def num():
#     return [lambda x: i*x for i in range(4)]
# print(num())
# print([m(2) for m in num()])


# def test1():
#     global a
#     a = 1
#     a += 1
#     b = 1
#     print(a+b)
#
#     def test2():
#         # nonlocal b
#         # b += 1
#         print(a + b)
#
#         def test3():
#             global a
#             nonlocal b
#             a += 99
#             b += 99
#             print(a+b)
#
#         test3()
#
#     test2()
#
# test1()
#
# def testa():
#     global a
#     a += 99999
#     print(a)
#
# testa()

# li = ['1','2','3']
# lis = list(map(lambda x:int(x),li))
# # lis= []
# # for i in li:
# #     lis.append(int(i))
# print(lis)

a = [1,2,3,4,1,2]
b=[999,777]
print(dir(a))
a.reverse()
# print(a)
# print(a.index(2))
# a.extend(b)
# print(a)

# print([i**2 for i in range(1,11)])









# a = [i for i in range(10)]
# print(a.index(0))
# print(a.count(0))


