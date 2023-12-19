# coding = utf-8

def sequentialSearch(list, item):
    pos = 0
    found = False

    while pos < len(list) and not found:
        if list[pos] != item:
            pos += 1
        else:
            found = True
    return found


if __name__ == "__main__":
    list = [9,8,7,6,5,4,3,2,1,0]
    result = sequentialSearch(list, 7)
    print(result)
    b = [i for i in range(0,10)]
    a = b[0:5]
    c = [i for i in range(0,10,3)]
    print(b)
    print(a)
    print(c)

