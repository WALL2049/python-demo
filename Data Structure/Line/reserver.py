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
    node = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))

    root = Reserver(node)

    while root:
        print(root.data)
        root = root.next