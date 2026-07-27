queue = []
MAX_SIZE = 5

def enqueue():
    if len(queue) == MAX_SIZE:
        print("Parking is Full! No space for new cars.")
    else:
        car = input("Enter Car Number: ")
        queue.append(car)
        print(car, "has entered the parking.")

def dequeue():
    if len(queue) == 0:
        print("Parking is Empty! No cars to leave.")
    else:
        car = queue.pop(0)
        print(car, "has left the parking.")

def display():
    if len(queue) == 0:
        print("Parking is Empty.")
    else:
        print("Cars in Parking Queue:")
        for car in queue:
            print(car)

while True:
    print("\n--- Traffic Management System ---")
    print("1. Enqueue (Car Entry)")
    print("2. Dequeue (Car Exit)")
    print("3. Display Cars")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice! Please try again.")
