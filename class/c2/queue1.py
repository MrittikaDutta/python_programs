queue = []

def is_empty():
    return len(queue) == 0

def enqueue(item):
    queue.append(item)

def dequeue():
    if is_empty():
        return "Queue is empty. Cannot perform dequeue."
    return queue.pop(0)

def peek():
    if is_empty():
        return "Queue is empty."
    return queue[0]

def size():
    return len(queue)

def user_interaction():
    while True:
        print("\n1. Enqueue (Add)")
        print("2. Dequeue (Remove)")
        print("3. Peek (Front Item)")
        print("4. Check if Empty")
        print("5. Get Size")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            enqueue(item)
            print(f"Enqueued {item} to the queue.")
        elif choice == '2':
            print("Dequeued item:", dequeue())
        elif choice == '3':
            print("Front item:", peek())
        elif choice == '4':
            print("Is the queue empty?", is_empty())
        elif choice == '5':
            print("Size of the queue:", size())
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    user_interaction()
