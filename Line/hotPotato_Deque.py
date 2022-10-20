from class_Deque import Deque

def hotPotato(namelist, num):
    hotDeque = Deque()
    for name in namelist:
        hotDeque.addRear(name)

    while hotDeque.size() > 1:
        for i in range(num):
            hotDeque.addRear(hotDeque.removeFront())
        hotDeque.removeFront()
    return hotDeque.removeFront()


if __name__ == '__main__':
    luckyone = hotPotato(['Jack', 'Nancy', 'Lily', 'Tony', 'Bob', 'Mark', 'Mike', 'Marry'], 7)
    print(luckyone)

