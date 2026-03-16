class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None 
    cur = head  
    while cur is not None:
        next_node = cur.next

        cur.next = prev
        prev = cur          
        cur = next_node 
    
    return prev



head = node(10)
head.next = node(20)
head.next.next = node(30)
head.next.next.next = node(40)
head.next.next.next.next = node(50)

new = reverse(head)

temp = new
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")