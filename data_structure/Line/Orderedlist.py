# coding=utf-8
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class Unorderedlist:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head

        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def index(self, item):
        count = 0
        current = self.head
        found = False

        while current.getData() != item:
            if current.getData() == None:
                return False
            else:
                count = count + 1
                current = current.getNext()
        else:
            return count


    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            previous.setNext(temp)
            temp.setNext(current)


    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found


    def remove(self, item):
        current = self.head
        previous = None
        exit = True

        while current.getData() != item and exit:
            if current.getData() < item:
                previous = current
                current = current.getNext()
            else:
                exit = False
                return exit
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


    def pop(self):
        current = self.head
        previous = None

        if self.head == None:
            self.head = temp
            return False

        while current.getNext() != None:
            previous = current
            current = current.getNext()
        else:
            previous.setNext(None)





if __name__ == '__main__':
    mylist = Unorderedlist()
    mylist.add(31)
    mylist.add(93)
    mylist.add(54)
    print(mylist.size())

    mylist.remove(54)
    print(mylist.size())



