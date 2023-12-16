# dict d
# set s

# s.add()
# s.remove()
#
# d.get(key)
# d[key]
#
# d.keys()
# d.values()
# d[]= ''
# d.pop(key)
# d.popitems()
# for key, values in d.items()
#
# get(key) 方法在 key（键）不在字典中时，可以返回默认值 None 或者设置的默认值。
#
# dict[key] 在 key（键）不在字典中时，会触发 KeyError 异常。


# d = {'k1':'v1', 'k2':'v2', 'k3':'v3333'}
# d['k3'] = 'v3'
# # del d['k2']
# # d.popitem()
# print(d)

# l = [5,4,3,2,1]
# for index, value in enumerate(l):
#     print(f'{index} : {value}')

# strs = ["flower","flow","flight"]
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:

# def isPalindrome(self, head: ListNode) -> bool:
#     current = head
#     l = []
#     while current != None:
#         num = current.val
#         l.append(num)
#         current = current.next
#     return k == l[::-1]
#
#
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         vals = []
#         current_node = head
#         while current_node is not None:
#             vals.append(current_node.val)
#             current_node = current_node.next
#         return vals == vals[::-1]


# a = [0,1,2,3,4,5,6,7,8]


# def countnum(a):
#     # sumnum = 0
#     # for i in a :
#     #     if i%2 == 0:
#     #         sumnum += 1
#     # print(sumnum)
#     # def fun(x):
#     #     return x%2 == 0
#     # print(list(filter(fun, a)))
#
#     print(list(filter(lambda x :x%2 ==0, a)))
#
# countnum(a)


import os

# 一层目录
filelist = os.listdir('D:\myfiles\研究生课件')
print(filelist)

# 多层目录
for root, dirs, files in os.walk('D:\myfiles\研究生课件'):
    # 文件夹
    for dir in dirs:
        print(os.path.join(root, dir))
    # 文件
    for file in files:
        print(os.path.join(root, file))
