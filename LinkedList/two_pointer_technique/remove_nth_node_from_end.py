"""

"""
from LinkedList.singly_linked_list.design_linked_list import LinkedList


def remove_nth_from_end(head, size, n):
    last_ind = size - 1
    curr = head
    steps = last_ind - n
    if steps < 0:
        head = curr.next
        # curr = None
        return head
    while steps > 0:
        curr = curr.next
        steps -= 1
    # node_to_delete = curr.next
    curr.next = curr.next.next
    # node_to_delete = None
    return head


cases = [([1, 2], 2), ([1, 2, 3, 4, 5, 6, 7], 3), ([1], 1), ([1, 2, 3, 4, 5, 6, 7], 7)]
for case in cases:
    ll = LinkedList()
    values = case[0]
    n = case[1]
    for val in values:
        ll.addAtTail(val)
    new_head = remove_nth_from_end(ll.head, ll.size, n)

    curr = new_head
    if not curr:
        print("LinkedList is empty", end="")
    while curr:
        print("{}".format(curr.value), end=" --> ")
        curr = curr.next
    print()


