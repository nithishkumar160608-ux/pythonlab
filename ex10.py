heap = []

def insert(job, priority):
    heap.append((priority, job))
    i = len(heap) - 1

    while i > 0:
        parent = (i - 1) // 2
        if heap[i][0] < heap[parent][0]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break

def extract_min():
    if not heap:
        print("Heap is empty")
        return

    min_job = heap[0]
    heap[0] = heap[-1]
    heap.pop()

    i = 0
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < len(heap) and heap[left][0] < heap[smallest][0]:
            smallest = left

        if right < len(heap) and heap[right][0] < heap[smallest][0]:
            smallest = right

        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
        else:
            break

    print("Deleted Job:", min_job[1])
    print("Priority:", min_job[0])

def peek():
    if heap:
        print("Highest Priority Job:", heap[0][1])
        print("Priority:", heap[0][0])
    else:
        print("Heap is empty")

def display():
    if not heap:
        print("Heap is empty")
    else:
        print("Jobs in Heap Order:")
        for priority, job in heap:
            print(job, "-", priority)

while True:
    print("\n1. Insert Job")
    print("2. Delete Highest Priority Job")
    print("3. Peek Highest Priority Job")
    print("4. Display All Jobs")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        job = input("Enter job name: ")
        priority = int(input("Enter priority: "))
        insert(job, priority)
        print("Job inserted")

    elif choice == 2:
        extract_min()

    elif choice == 3:
        peek()

    elif choice == 4:
        display()

    elif choice == 5:
        break

    else:
        print("Invalid choic
