class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def insert_bst(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert_bst(root.left , value)
    elif value > root.value:
        root.right = insert_bst(root.right, value)

    return root




root = None

values = [10, 5, 15, 3, 7, 12, 18]

for v in values:
    root = insert_bst(root, v)