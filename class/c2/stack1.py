stack=[]
def is_empty():
    return len(stack) == 0

def push(item):
    stack.append(item)
def disp():
    for i in stack:
        print(i)

def pop():
    if is_empty():
        return "Stack is empty. Cannot perform pop."
    return stack.pop()

def peek():
    if is_empty():
        return "Stack is empty."
    return stack[-1]

def size():
    return len(stack)
while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if Empty")
    print("5. display")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
            
    if choice == '1':
        item = input("Enter the item to push: ")
        push(item)
        print(f"Pushed {item} to the stack.")
    elif choice == '2':
        print("Popped item:", pop())
    elif choice == '3':
        print("Top item:", peek())
    elif choice == '4':
        print("Is the stack empty?", is_empty())
    elif choice == '5':
        disp()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
            