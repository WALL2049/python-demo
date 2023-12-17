from Queue import Queue

def hotPotato(namelist, num):
    hotQueue = Queue()
    for name in namelist:
        hotQueue.enqueue(name)
    print(hotQueue.items)
    while hotQueue.size() > 1:
        for i in range(num):
            hotQueue.enqueue(hotQueue.dequeue())
            print(hotQueue.items)
        hotQueue.dequeue()
        print(hotQueue.items)
    return hotQueue.dequeue()


if __name__ == '__main__':
    luckyone = hotPotato(['Jack', 'Nancy', 'Lily', 'Tony', 'Bob', 'Mark'], 7)
    print(luckyone)