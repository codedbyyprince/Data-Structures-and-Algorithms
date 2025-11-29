class node:
    def __init__(self,data):
        self.data = data 
        self.next = None

# --------delete-at-beginning------------
def delete_at_begining(head):
    if head is None:
        return None 
    temp = head 
    head = head.next 
    temp = None
    return head 

# --------delete-at-end------------------
def delete_at_end(head):
    if head is None:
        return None
    
    if head.next is None:
        return None
    
    temp = head
    while temp.next.next is not None:
        temp = temp.next

    temp.next = None
    return head

# --------delete-at-specific-point--------
def delete_at_specific(head, pos):
    if head is None:
        return None
    
    if pos == 1:
        temp = head
        head = head.next
        temp = None
        return head
    
    temp = head
    count = 1
    while temp is not None and count < pos -1 :
        temp = temp.next
        count += 1

    if temp is None or temp.next is None:
        return head 
    
    delete_node = temp.next 
    temp.next = delete_node.next 
    delete_node = None

    return head

head = node(10)
head.next = node(20)
head.next.next = node(30)
head.next.next.next = node(40)
head.next.next.next.next = node(50)

head = delete_at_begining(head)
head = delete_at_end(head)

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")