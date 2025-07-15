stack = []

def push(e):
    stack.append(e)
    print(f"{e} Pushed")


def pop():
    if not stack:
        print("Stack is empty. Cannot pop.")
    else:
        e= stack.pop()
        print(f"{e} Popped")


def display_stack():
    if not stack:
        print("Stack is empty.")
    else:
        print("Current stack:", stack)


while True:
    print("\nChoose an option:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Quit")
    c = input("Enter your choice : ")

    if c == '1':
        e= input("Enter the element to push onto the stack: ")
        push(e)
    elif c== '2':
        pop()
    elif c== '3':
        display_stack()
    elif c== '4':
        print("Exit")
        break
    else:
        print("Invalid choice.")