class node: 
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key 

# Initializing and allocating memory for tree nodes
first_node = node(10)
sec_node = node(20)
third_node = node(30)
forth_node = node(40)
fifth_node = node(80)
six_node = node(60)
seventh_node = node(90)

# creating nodes 
first_node.right = sec_node
first_node.left = third_node

third_node.left = six_node
third_node.right = seventh_node

sec_node.left = forth_node
sec_node.right = fifth_node