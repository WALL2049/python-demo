# coding=utf-8
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

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

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

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

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found


    def remove(self, item):
        current = self.head
        previous = None
        found = False
        # while not found:
        #     if current.getData() == item:
        #         found = True
        #         if previous == None:
        #             self.head = current.getNext()
        #         else:
        #             previous.setNext(current.get())        #这样写的话似乎不对，previous还没实例化，没法用这个方法，所以可以提出去
        #     else:
        #         previous = current
        #         current = current.getNext()


        while current.getData() != item:
            previous = current
            current = current.getNext()
        else:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

                # if previous == None:
        #     self.head = current.getNext()
        # else:
        #     previous.setNext(current.getNext())



    def append(self, item):
        temp = Node(item)
        current = self.head
        found = False

        if self.head == None:
            self.head = temp
            return

        while current.getNext() != None:
            current = current.getNext()
        else:
            current.setNext(temp)

    def insert(self, pos, item):
        temp = Node(item)
        count = 0
        current = self.head
        previous = None
        while count != pos:
            previous = current
            current = current.getNext()
            count = count + 1
        else:
            previous.setNext(temp)
            temp.setNext(current)

    def pop(self, pos = 0):
        count = 0
        current = self.head
        previous = None
        while count != pos:
            previous = current
            current = current.getNext()
            count = count + 1
        else:
            if count == 0:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    def printlist(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()





if __name__ == '__main__':
    mylist = Unorderedlist()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    # print(mylist.size())
    # print(mylist.search(93))
    # print(mylist.index(93))
    # print(mylist.search(100))
    #
    # mylist.add(100)
    # print(mylist.search(100))
    # print(mylist.size())
    #
    # mylist.remove(54)
    # print(mylist.size())
    # mylist.remove(93)
    # print(mylist.size())
    # mylist.remove(31)
    # print(mylist.size())
    # print(mylist.search(93))
    #
    # mylist.append(88)
    # print(mylist.size())
    # mylist.add(66)
    # print(mylist.size())
    # mylist.pop(0)
    # print(mylist.search(66))
    # print(mylist.size())