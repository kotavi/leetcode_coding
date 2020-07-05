class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def print_linked_list(self):
        curr = self.head
        if not curr:
            print("LinkedList is empty")
            return
        while curr:
            print("{}".format(curr.value), end=" --> ")
            curr = curr.next
        print()

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        if not self.head:
            return -1
        curr = self.head
        while index > 0:
            curr = curr.next
            index -= 1
        return curr.value

    def addAtHead(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def addAtIndex(self, index, data):
        curr = self.head
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(data)
        elif index == self.size:
            self.addAtTail(data)
        else:
            while index > 1:
                curr = curr.next
                index -= 1
            new_node = Node(data)
            new_node.next = curr.next
            curr.next = new_node
            self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        curr = self.head
        if index == 0:
            self.head = curr.next
            curr = None
        else:
            while index > 1:
                curr = curr.next
                index -= 1

            node_to_delete = curr.next
            curr.next = curr.next.next
            node_to_delete = None
        self.size -= 1


def test(commands, values):
    obj = LinkedList()
    switcher = {
        "addAtHead": "obj.addAtHead(value)",
        "addAtTail": "obj.addAtTail(value)",
        "addAtIndex": "obj.addAtIndex(index, value)",
        "deleteAtIndex": "obj.deleteAtIndex(index)",
        "get": "obj.get(index)",
        "print": "obj.print_linked_list()"
    }
    for i in range(len(commands)):
        command = commands[i]
        list_values = values[i]
        if len(list_values) == 2:
            index = list_values[0]
            value = list_values[1]
        elif command in ["get", "deleteAtIndex"]:
            index = list_values[0]
        else:
            value = list_values[0]
        exec(switcher["print"])
        exec(switcher[command])


if __name__ == "__main__":

    print("Test1: ")
    c = ["addAtHead", "addAtTail", "addAtTail", "get", "get", "addAtTail", "addAtIndex", "addAtHead", "addAtHead",
         "addAtTail", "addAtTail", "addAtTail", "addAtTail", "get", "addAtHead", "addAtHead", "addAtIndex",
         "addAtIndex", "addAtHead", "addAtTail", "deleteAtIndex", "addAtHead", "addAtHead", "addAtIndex", "addAtTail",
         "get", "addAtIndex", "addAtTail", "addAtHead", "addAtHead", "addAtIndex", "addAtTail", "addAtHead",
         "addAtHead", "get", "deleteAtIndex", "addAtTail",  "addAtTail", "addAtHead", "addAtTail", "get",
         "deleteAtIndex", "addAtTail", "addAtHead", "addAtTail",  "deleteAtIndex", "addAtTail", "deleteAtIndex",
         "addAtIndex", "deleteAtIndex", "addAtTail", "addAtHead",  "addAtIndex", "addAtHead", "addAtHead", "get",
         "addAtHead", "get", "addAtHead", "deleteAtIndex", "get", "addAtHead", "addAtTail", "get", "addAtHead", "get",
         "addAtTail", "get", "addAtTail", "addAtHead", "addAtIndex",  "addAtIndex", "addAtHead", "addAtHead",
         "deleteAtIndex", "get", "addAtHead", "addAtIndex", "addAtTail", "get", "addAtIndex", "get", "addAtIndex",
         "get", "addAtIndex", "addAtIndex", "addAtHead", "addAtHead", "addAtTail", "addAtIndex", "get", "addAtHead",
         "addAtTail", "addAtTail", "addAtHead", "get", "addAtTail", "addAtHead", "addAtTail", "get", "addAtIndex"]
    v = [[84], [2], [39], [3], [1], [42], [1, 80], [14], [1], [53], [98], [19], [12], [2], [16], [33], [4, 17], [6, 8],
         [37], [43], [11], [80], [31], [13, 23], [17], [4], [10, 0], [21], [73], [22], [24, 37], [14], [97], [8], [6],
         [17], [50], [28], [76], [79], [18], [30], [5], [9], [83], [3], [40], [26], [20, 90], [30], [40], [56],
         [15, 23], [51], [21], [26], [83], [30], [12], [8], [4], [20], [45], [10], [56], [18], [33], [2], [70], [57],
         [31, 24], [16, 92], [40], [23], [26], [1], [92], [3, 78], [42], [18], [39, 9], [13], [33, 17], [51], [18, 95],
         [18, 33], [80], [21], [7], [17, 46], [33], [60], [26], [4], [9], [45], [38], [95], [78], [54], [42, 86]]
    test(c, v)

    print("\nTest 2:")
    c = ["addAtHead", "addAtIndex", "addAtTail", "addAtHead", "addAtIndex", "addAtTail", "addAtTail",
         "addAtIndex", "deleteAtIndex", "deleteAtIndex", "addAtTail"]
    v = [[0], [1, 4], [8], [5], [4, 3], [0], [5], [6, 3], [7], [5], [4]]
    test(c, v)

    print("\nTest 3:")
    c = ["addAtHead", "addAtIndex", "get", "addAtHead", "addAtTail", "get", "addAtTail", "get", "addAtHead",
     "get", "addAtHead"]
    v = [[5], [1, 2], [1], [6], [2], [3], [1], [5], [2], [2], [6]]
    test(c, v)

    print("\nTest 4:")
    c = ["addAtHead", "addAtHead", "addAtHead", "addAtHead", "addAtHead",
         "deleteAtIndex", "deleteAtIndex", "deleteAtIndex", "deleteAtIndex"]
    v = [[0], [8], [5], [10], [5], [4], [3], [2], [1]]
    test(c, v)

    print("\nTest 5:")
    c = ["addAtHead", "deleteAtIndex"]
    v = [[1], [0]]
    test(c, v)

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.addAtHead("apple")
#     ll.addAtHead("tea")
#     ll.addAtHead(56)
#     ll.addAtHead(-10)
#     ll.print_linked_list()
#     print("\nTail: {}".format(ll.tail.value))
#     for i in range(ll.size+1):
#         print("Get at {}: {}".format(i, ll.get(i)))
#
#     print("\nDeleting at 0 index:")
#     for _ in range(ll.size):
#         ll.deleteAtIndex(0)
#         ll.print_linked_list()
#
#     for i in range(10):
#         ll.addAtHead(i)
#     ll.print_linked_list()
#     print("\nDeleting at 0 index:")
#     for _ in range(ll.size):
#         ll.deleteAtIndex(2)
#         ll.print_linked_list()
#
#     for i in range(10):
#         ll.addAtHead(i)
#     ll.print_linked_list()
#     print("\nDeleting last node:")
#     for _ in range(ll.size):
#         ll.deleteAtIndex(ll.size-1)
#         ll.print_linked_list()
#
#     print("- * " * 15)
#     ll2 = LinkedList()
#     ll2.addAtHead(1)
#     ll2.addAtTail(3)
#     ll2.addAtIndex(1, 2)
#     ll2.print_linked_list()
#     print(ll2.get(1))
#     print("-----\n", ll2.size, ll2.tail.value)
#     ll2.deleteAtIndex(1)
#     print(ll2.get(1))
