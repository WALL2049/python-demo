class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)
        # self.insert(0, item)

    def pop(self, item):
        return self.items.pop()
        # return self.pop(1)

    def peek(self):
        return self.items[-1]


if __name__ == '__main__':
    list1 = [0,1,2]
    print(list1.pop())