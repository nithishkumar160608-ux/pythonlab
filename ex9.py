class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.left = None
        self.right = None
        self.height = 1


def height(n):
    return n.height if n else 0


def balance(n):
    return height(n.left) - height(n.right) if n else 0


def right_rotate(y):
    x = y.left
    t = x.right
    x.right = y
    y.left = t

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x


def left_rotate(x):
    y = x.right
    t = y.left
    y.left = x
    x.right = t

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y


def insert(root, id, name):
    if root is None:
        return Node(id, name)

    if id < root.id:
        root.left = insert(root.left, id, name)
    elif id > root.id:
        root.right = insert(root.right, id, name)
    else:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    b = balance(root)

    if b > 1 and id < root.left.id:
        return right_rotate(root)

    if b < -1 and id > root.right.id:
        return left_rotate(root)

    if b > 1 and id > root.left.id:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if b < -1 and id < root.right.id:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def min_node(root):
    while root.left:
        root = root.left
    return root


def delete(root, id):
    if root is None:
        return root

    if id < root.id:
        root.left = delete(root.left, id)

    elif id > root.id:
        root.right = delete(root.right, id)

    else:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        temp = min_node(root.right)
        root.id = temp.id
        root.name = temp.name
        root.right = delete(root.right, temp.id)

    root.height = 1 + max(height(root.left), height(root.right))
    b = balance(root)

    if b > 1 and balance(root.left) >= 0:
        return right_rotate(root)

    if b > 1 and balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if b < -1 and balance(root.right) <= 0:
        return left_rotate(root)

    if b < -1 and balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def search(root, id):
    if root is None or root.id == id:
        return root

    if id < root.id:
        return search(root.left, id)

    return search(root.right, id)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.id,"-",root.name)
        inorder(root.right)
def preorder(root):
    if root:
        print(root.id,"-",root.name)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.id,"-",root.name)


def count(root):
    if root is None:
        return 0
    return 1 + count(root.left) + count(root.right)


root = None

while True:
    print("\n--- AVL TREE ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Count")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        id = int(input("Enter Enrollment ID: "))
        name = input("Enter Student Name: ")
        root = insert(root, id, name)
        print("Record inserted")

    elif ch == 2:
        id = int(input("Enter Enrollment ID: "))
        if search(root, id):
            root = delete(root, id)
            print("Record deleted")
        else:
            print("Record not found")

    elif ch == 3:
        id = int(input("Enter Enrollment ID: "))
        result = search(root, id)

        if result:
            print("Found:", result.id, "-", result.name)
        else:
            print("Record not found")

    elif ch == 4:
        print("Records in Inorder:")
        inorder(root)
        print("Records in Preorder:")
        preorder(root)
        print("Records in Postorder:")
        postorder(root)



    elif ch == 5:
        print("Total Enrollments:", count(root))

    elif ch == 6:
        print("Program ended")
        break

    else:
        print("Invalid choice")
