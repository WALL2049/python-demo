# coding=utf-8
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def Reserver(link):
    pre = link
    cur = link.next
    pre.next = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre


if __name__ == "__main__":

    root = Reserver(node)

    while root:
        print(root.data)
        root = root.next