class ListDemo1:
    def __init__(self):
        pass


if __name__ == "__main__":
    firstList = [1,2,3,4]
    secondList = [7,77,777]
    firstList.append(9)
    firstList.insert(0,100)
    firstList.extend(secondList)
    print(firstList)

    firstList.pop()
    print(firstList)
    firstList.pop(1)
    print(firstList)
    firstList.remove(100)
    print(firstList)
    secondList.clear()
    print(secondList)

    firstList[0] = 12345678
    print(firstList)

    firstList.sort()
    print(firstList)

    secondList = [2,34,66,32,1,1,676,9,34,1,234,1,2]
    print(secondList.index(1))
    lastList = sorted(secondList)
    print(lastList)

    for index, item in enumerate(lastList):
        # print(index, "=", item)
        print(f"{index} = {item}", end = "\t")
    print(secondList.count(1))

    tup1 = tuple(firstList)
    print(tup1)
    list1 = list(tup1)
    print(list1)
    print(list1+list1)
    str1 = "qwefasfas"
    print(list(str1))
    print(list1[1:3])