class LinkedList:
    def __init__(self,v=0,next=None):
        self.value=v
        self.next=next
def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
def inputLL():
    head=None
    tail=None
    values = input("Enter the elements  separated by space: ").split()
    for value in values:
        if not head:
            head = LinkedList(int(value))
            tail = head
        else:
            tail.next = LinkedList(int(value))
            tail = tail.next
        return head
def middleLL(head):
    s=head
    f=head
    while f and f.next:
        s=s.next
        f=f.next.next
    return s




if __name__ == "__main__":
    head = inputLL()
    print_list(head)

    middle_node = middleLL(head)
    print(f"The middle node is: ",middle_node.value)