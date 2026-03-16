class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# traversal

def traverselist(head):
    while head is not None:
        print(head.data, end='')
        if head.next is not None:
            print('-->', end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    traverselist(head)