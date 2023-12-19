class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)
        # self.items.inset(0, item)

    def dequeue(self, item):
        return self.items.pop(0)
        # self.items.pop()

    def size(self):
        return len(self.items)