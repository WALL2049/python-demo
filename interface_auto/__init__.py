url = 'www.baidu.com'

a = url.split('.')[-2]
print(a)
print('\n\n-------- HTTP response * begin -------')

dict = {'Google': 'www.google.com',
        'Baidu': 'www.baidu.com',
        'taobao': 'www.taobao.com'}

# 将字典类型转换为可遍历的元组
# print("字典值: %s" %dict.items())
print(f"字典值: {dict.items()}")

# 遍历字典列表
# python for a,b in c, in后面的是一个元祖数组,比如这种 [(1,4),(2,5),(3,6)], 那么a,b就分别返回1,4然后2,5然后3,6
for key,values in dict.items():
    print(f'{key} : {values}')
