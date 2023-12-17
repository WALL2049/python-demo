class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def reverse_list(head):
    previous = None
    current = head
    while current:
        temp = current.next
        current.next = previous
        previous = current
        current = temp

    return previous


if __name__ == "__main__":
    def print_list(head):
        while head:
            print(head.data)
            head = head.next

    head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))

    print(print_list(head))
    reverse_head = reverse_list(head)
    print(print_list(reverse_head))
