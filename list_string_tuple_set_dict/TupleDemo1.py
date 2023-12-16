class TupleDemo1:
    def __init__(self):
        pass



if __name__ == "__main__":
    tup1 = (1,2,3,4,4,7,77)
    print(tup1.count(4))
    tup2 = (7,77,777)
    print(tup1 + tup2)
    print(tup1.index(4))
    print(tup1[1])
    str1 = "abcdefg"
    print(tuple(str1))
    print(tup1[1:3])