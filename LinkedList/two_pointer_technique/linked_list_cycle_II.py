"""
Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.

To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to. If pos is -1,
then there is no cycle in the linked list.

Note: Do not modify the linked list.

Approach:
- Phase1:
If there is a loop in Linked List, then return the node where pointer meet (intersection point)
- Phase2:
Start traversing the LL from head and from intersection point,
the node where they meet is the start of the loop
"""
from LinkedList.singly_linked_list.design_linked_list import LinkedList, Node


def find_intersect(head):
    """
    :param head: the pointer to the first node of the Linked List
    :return: Node where pointers meet in case of the loop, None - in case there is no loop
    """
    slow = fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None


def detect_cycle(head):
    intersect = find_intersect(head)
    if not intersect:
        return None
    pointer1 = head
    pointer2 = intersect
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


def create_cycle(head, index):
    curr = head
    while curr.next:
        curr = curr.next
    last_node = curr

    curr = head
    # find node under defined index
    while index > 0:
        curr = curr.next
        index -= 1

    # create a  cycle
    cycle_start = curr
    last_node.next = cycle_start

    return head


ll = LinkedList()
lst, index = [-3, -2, -1, 0, 1, 0, 2, 3, 4, 5, 23, -10, 45, 90, 16], 9
for el in lst:
    ll.addAtTail(el)
print("Linked List:")
ll.print_linked_list()

head = create_cycle(ll.head, index)
intersection = find_intersect(head)
print("Slow and fast pointers intersect in: ", intersection.value)

cycle = detect_cycle(head)
print("Cycle starts from here: ", cycle.value)

print("-#-" * 15)
ll = LinkedList()
lst, index = [2, 4, 6, 8, 0, 1, 3, 5, 7, 9], 4
for el in lst:
    ll.addAtTail(el)
print("Linked List:")
ll.print_linked_list()

head = create_cycle(ll.head, index)
intersection = find_intersect(head)
print("Slow and fast pointers intersect in: ", intersection.value)

cycle = detect_cycle(head)
print("Cycle starts from here: ", cycle.value)
