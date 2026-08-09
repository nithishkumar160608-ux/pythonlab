class Node:
    def _init_(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None

def insert(head, coeff, power):
    new = Node(coeff, power)
    if head is None:
        return new
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new
    return head

def display(head):
    temp = head
    while temp:
        print(f"{temp.coeff}x^{temp.power}", end="")
        if temp.next:
            print(" + ", end="")
        temp = temp.next
    print()

def add(p1, p2):
    result = None

    while p1 and p2:
        if p1.power == p2.power:
            result = insert(result, p1.coeff + p2.coeff, p1.power)
            p1 = p1.next
            p2 = p2.next
        elif p1.power > p2.power:
            result = insert(result, p1.coeff, p1.power)
            p1 = p1.next
        else:
            result = insert(result, p2.coeff, p2.power)
            p2 = p2.next

    while p1:
        result = insert(result, p1.coeff, p1.power)
        p1 = p1.next

    while p2:
        result = insert(result, p2.coeff, p2.power)
        p2 = p2.next

    return result

p1 = None
n1 = int(input("Enter number of terms in Polynomial 1: "))
print("Enter coefficient and power:")
for i in range(n1):
    c = int(input("Coefficient: "))
    p = int(input("Power: "))
    p1 = insert(p1, c, p)

p2 = None
n2 = int(input("\nEnter number of terms in Polynomial 2: "))
print("Enter coefficient and power:")
for i in range(n2):
    c = int(input("Coefficient: "))
    p = int(input("Power: "))
    p2 = insert(p2, c, p)

print("\nPolynomial 1:")
display(p1)

print("Polynomial 2:")
display(p2)

result = add(p1, p2)

print("Resultant Polynomial:")
display(result)
