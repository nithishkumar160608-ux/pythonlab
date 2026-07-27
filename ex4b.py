class Node:
    def _init_(self, car_number):
        self.car_number = car_number
        self.next = None



class Queue:
    def _init_(self):
        self.front = None
        self.rear = None


    def enqueue(self, car_number):
        new_node = Node(car_number)

        if self.rear is None:
            self.front = self.rear = new_node
            print(f"Car {car_number} entered the parking.")
            return

        self.rear.next = new_node
        self.rear = new_node
        print(f"Car {car_number} entered the parking.")

    def dequeue(self):
        if self.front is None:
            print("Parking is empty. No car to exit.")
            return

        exited_car = self.front.car_number
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print(f"Car {exited_car} exited the parking.")

    def display(self):
        if self.front is None:
            print("Parking is empty.")
            return

        print("\nCars currently in parking:")
        temp = self.front
        while temp:
            print(temp.car_number, end=" -> ")
            temp = temp.next
        print("None")


parking = Queue()

while True:
    print("\n--- Car Parking Management System ---")
    print("1. Car Entry (Enqueue)")
    print("2. Car Exit (Dequeue)")
    print("3. Display Parked Cars")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        car = input("Enter Car Number: ")
        parking.enqueue(car)

    elif choice == 2:
        parking.dequeue()

    elif choice == 3:
        parking.display()

    elif choice == 4:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.")
