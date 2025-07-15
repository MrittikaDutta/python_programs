class CustomQueue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if not self.is_full():
            self.queue.append(item)
            print(f"Enqueued: {item}")
        else:
            print("Queue is full. Cannot enqueue.")

    def dequeue(self):
        if self.queue:
            item = self.queue.pop(0)
            print(f"Dequeued: {item}")
        else:
            print("Queue is empty. Cannot dequeue.")

    def display(self):
        print("Queue:", self.queue)



max_size = int(input("Enter the maximum size of the queue: "))
queue = CustomQueue(max_size)

while True:
    print("\nMenu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display Queue")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        item = input("Enter item to enqueue: ")
        queue.enqueue(item)
    elif choice == "2":
        queue.dequeue()
    elif choice == "3":
        queue.display()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
