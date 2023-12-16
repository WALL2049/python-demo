class StringListTupleDemo:
    def __init__(self):
        pass


if __name__ == "__main__":
    tup1 = (1, 2, "a", "b", 3)
    list1 = list(tup1)
    print(list1)
    tup2 = tuple(list1)
    print(tup2)
    str1 = "ab23b53"
    list2 = list(str1)
    print(list2)
    list3 = str1.split("3")
    print(list3)
    str2 = "-".join(list3)
    print(str2)
    tup3 = tuple(str2)
    print(tup3)
    a = 6867
    str3 = str(a)
    print(str3)
    print(int(str3) - 1)