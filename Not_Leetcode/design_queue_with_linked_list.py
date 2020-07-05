class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        first_node = self.head
        second_node = first_node.next
        self.head = second_node
        first_node.next = None
        self.size -= 1

    def print_linked_list(self):
        curr = self.head
        while curr:
            print("{}".format(curr.val), end=" --> ")
            curr = curr.next


if __name__ == '__main__':
    ll = Queue()
    assert ll.is_empty() is True
    print("Enqueue:")
    ll.enqueue(23)
    ll.enqueue(-1)
    ll.enqueue(5)
    ll.enqueue(11)

    ll.print_linked_list()

    print("\nDequeue:")
    ll.dequeue()
    ll.print_linked_list()

    print("\nEnqueue:")
    ll.enqueue(13)
    ll.enqueue(-7)
    ll.print_linked_list()

    print("\nDequeue:")
    ll.dequeue()
    ll.print_linked_list()

    print("\nDequeue all but not the last:")
    ll.dequeue()
    ll.dequeue()
    ll.dequeue()
    ll.print_linked_list()
