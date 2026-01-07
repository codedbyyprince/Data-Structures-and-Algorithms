class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def insert_bst(root, value):
    if root is None:
        return Node(value)
    if value < root.val:
        root.left = insert_bst(root.left , value)
    elif value > root.val:
        root.right = insert_bst(root.right, value)

    return root


def bst_search(root, key):
    if root is None:
        return False
    
    if key == root.val:
        True
    elif key < root.val:
        return bst_search(root.left, key)
    else:
        return bst_search(root.right, key)


root = None
values = [10, 5, 15, 3, 7, 12, 18]

for v in values:
    root = insert_bst(root, v)

print(bst_search(root, 7))   # True
print(bst_search(root, 12))  # True
print(bst_search(root, 6))   # False
