class DictSortDemo1:
    def __init__(self):
        pass


if __name__ == "__main__":
    # Ҫ�󣺽��ĸ��˰��������С�����������
    d = {'����':23,'����':18,'����':20,'����':25}
    list1 = list(d.items())
    print(list1)
    list1.sort(key= lambda x:x[1], reverse=False)
    print(list1)
    list2 = sorted(list1, key = lambda x:x[1], reverse=True)
    print(list2)

