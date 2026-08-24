class Node:
    def __init__(self, name, time, purpose):
        self.name = name
        self.time = time
        self.purpose = purpose
        self.left = None
        self.right = None


class BST:
    def insert(self, root, name, time, purpose):
        if root is None:
            return Node(name, time, purpose)

        if name < root.name:
            root.left = self.insert(root.left, name, time, purpose)
        else:
            root.right = self.insert(root.right, name, time, purpose)

        return root

    def search(self, root, name):
        if root is None or root.name == name:
            return root

        if name < root.name:
            return self.search(root.left, name)
        return self.search(root.right, name)

    def delete(self, root, name):
        if root is None:
            return root

        if name < root.name:
            root.left = self.delete(root.left, name)
        elif name > root.name:
            root.right = self.delete(root.right, name)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            temp = root.right
            while temp.left:
                temp = temp.left

            root.name = temp.name
            root.time = temp.time
            root.purpose = temp.purpose
            root.right = self.delete(root.right, temp.name)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.name, root.time, root.purpose)
            self.inorder(root.right)

    def count(self, root):
        if root is None:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)


bst = BST()
root = None

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Count")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter visitor name: ")
        time = input("Enter entry time: ")
        purpose = input("Enter purpose: ")
        root = bst.insert(root, name, time, purpose)
        print("Entry inserted successfully.")

    elif choice == 2:
        name = input("Enter visitor name to search: ")
        result = bst.search(root, name)

        if result:
            print("Visitor found:", result.name, result.time, result.purpose)
        else:
            print("Visitor not found.")

    elif choice == 3:
        name = input("Enter visitor name to delete: ")
        root = bst.delete(root, name)
        print("Entry deleted successfully.")

    elif choice == 4:
        print("\nLog Entries in sorted order:")
        bst.inorder(root)

    elif choice == 5:
        print("Total entries:", bst.count(root))

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
