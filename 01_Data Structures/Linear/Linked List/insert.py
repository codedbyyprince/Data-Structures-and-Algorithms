class node:
    def __init__(self,data):
        self.data = data 
        self.next = None


# --------inset-at-start-----------------
def insert_at_start( head, data):
    newnode = node(data)
    newnode.next = head

    return newnode



# --------inset-at-end-----------------
def insert_at_end(head, data):
    newnode = node(data)

    if head is None:
        return newnode
    
    temp = head
    while temp.next is not None:
        temp = temp.next

    temp.next = newnode
    return head

# --------inset-at-specific-point-----------------
def insert_at_specific(head, pos , data):
    newnode = node(data)
    if pos == 1:
        newnode.next = head
        return newnode
    
    temp = head
    cur_pos = 1

    while temp is not None and cur_pos < pos - 1:
        temp = temp.next
        cur_pos += 1

    if temp is None:
        print('None')
        return head
    newnode.next = temp.next
    temp.next = newnode
    return head

head = node(10)
head.next = node(20)
head.next.next = node(30)

head = insert_at_start(head, 5)
head = insert_at_end(head, 15)
head = insert_at_specific(head, 3, 50)

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")