# a = [1]
# # b = [1]
# b = a
# # print(id(a))
# a.append(5)
#
# print(id(a))
# print(id(b))
# print(a)
# print(b)

# class MyClass(object):
#     def __init__(self, value):
#         self._value = value
#
#     @property
#     def value(self):
#         return self._value
#
#     @value.setter
#     def value(self, value):
#         self._value = value
#
#     @value.getter
#     def value(self):
#         return self._value
#
#     @value.deleter
#     def value(self):
#         del self._value


# c1 = MyClass(10)
# print(c1.value) # 10
# c1.value = 20
# print(c1.value) # 20
# del c1.value # _value成员被删除
# print(c1.value) # 报_value不存在的错误
#
# i = 1
# i += 1
# print(i)
#
# l = -1234
# k = list(str(l))
# if k[0] == '-':
#     k.pop(0)
#     j = k[::-1]
#     j.insert(0, '-')
# else:
#     j = k[::-1]
# print(j)
# a = ''.join(j)
# print(a)

# import re
# result = re.search('.doc', '123.doc')
# print(result.group())






