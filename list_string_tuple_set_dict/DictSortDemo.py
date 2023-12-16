class DictSortDemo1:
    def __init__(self):
        pass


if __name__ == "__main__":
    # 要求：将四个人按照年龄从小到大依次输出
    d = {'张三':23,'李四':18,'王五':20,'刘六':25}
    list1 = list(d.items())
    print(list1)
    list1.sort(key= lambda x:x[1], reverse=False)
    print(list1)
    list2 = sorted(list1, key = lambda x:x[1], reverse=True)
    print(list2)

