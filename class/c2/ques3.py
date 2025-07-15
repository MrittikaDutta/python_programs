class LinkedList:
    def __init__(self, v=0, next=None):
        self.value = v
        self.next = next
def inputLL():
    head = None
    tail = None
    values = input("enter elements separated by space: ").split()
    for i in values:
        if not head:
            head = LinkedList(int(i))
            tail = head
        else:
            tail.next = LinkedList(int(i))
            tail = tail.next

    return head


def middleLL(head):
    s = head
    f = head
    while f and f.next:
        s = s.next
        f = f.next.next
    return s
def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    head = inputLL()
    print_list(head)

    middle_node = middleLL(head)
    print(f"The middle node is: {middle_node.value}")
