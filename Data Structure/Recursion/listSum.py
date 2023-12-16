def listSum(numlist):
    if len(numlist) == 0:
        return False
    elif len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listSum(numlist[1:])


if __name__ == '__main__':
    print(listSum([1, 3, 5, 7, 9]))
    print(listSum([]))