# coding=utf-8

class DictSortDemo1:
    def __init__(self):
        pass


if __name__ == "__main__":
    # 要求：将四个人按照年龄从小到大依次输出
    d = {'张三':23,'李四':18,'王五':20,'刘六':25}
    # items()转成list排序
    list1 = list(d.items())
    print(list1)
    list1.sort(key= lambda x:x[1], reverse=False)
    print(list1)
    list2 = sorted(list1, key = lambda x:x[1], reverse=True)
    print(list2)
    print("============================")
    d1 = {"a": 3, "b": 2, "c": 1}
    # 按键排序返回列表
    result = sorted(d1.keys())
    print(result)
    # 按值排序返回列表
    result = sorted(d1.values())
    print(result)
    # 按键排序返回列表全部内容,这边建议还是先转化成list,list(d1.items())
    result = sorted(d1.items(), key=lambda x: x[0])
    print(result)
    # 按键排序返回列表全部内容
    result = sorted(d1.items(), key=lambda x: x[1])
    print(result)

    print(d1.items())
    print(type(d1.items()))
    for i in d1.items():
        print(i)