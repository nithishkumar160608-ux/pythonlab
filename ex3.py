class Node:
    def _init_(self, title):
        self.title = title
        self.next = None


class Stack:
    def _init_(self):
        self.top = None

   
    def push(self, title):
        new_node = Node(title)
        new_node.next = self.top
        self.top = new_node
        print(f'"{title}" has been added to the stack.')

   
    def pop(self):
        if self.top is None:
            print("Stack is empty. No book to retrieve.")
            return None

        removed_book = self.top.title
        self.top = self.top.next
        print(f'"{removed_book}" has been retrieved from the stack.')
        return removed_book

   
    def display(self):
        if self.top is None:
            print("Stack is empty.")
            return

        print("\nBooks in the stack (Top to Bottom):")
        current = self.top
        while current:
            print(current.title)
            current = current.next



stack = Stack()

while True:
    print("\n--- Library Management using Stack ---")
    print("1. Push (Add Book)")
    print("2. Pop (Retrieve Book)")
    print("3. Display Books")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter book title: ")
        stack.push(title)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.display()

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
