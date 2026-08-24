class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, data):
    if root is None:
        return Node(data)

    if data <= root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root
def search(root, data):
    if root is None:
        return False
    if root.data == data:
        return True
    elif data < root.data:
        return search(root.left, data)
    else:
        return search(root.right, data)
def minValueNode(root):
    current = root
    while current.left is not None:
        current = current.left
    return current
def delete(root, data):
    if root is None:
        return root
    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:        
        if root.left is None and root.right is None:
            return None    
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
root = None
n = int(input("Enter number of elements: "))
print("Enter the elements:")
for i in range(n):
    value = int(input())
    root = insert(root, value)
print("\nInorder Traversal:")
inorder(root)
print("\nPreorder Traversal:")
preorder(root)
print("\nPostorder Traversal:")
postorder(root)
key = int(input("\n\nEnter element to search: "))
if search(root, key):
    print("Element found")
else:
    print("Element not found")
key = int(input("Enter element to delete: "))
root = delete(root, key)
print("Inorder after deletion:")
inorder(root)