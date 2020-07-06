"""
https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

        a1 --> a2
                 \
                 c1 --> c2 --> c3
                 /
 b1 --> b2 --> b3

begin to intersect at node c1.
"""
from LinkedList.singly_linked_list.design_linked_list import LinkedList


def find_size(head):
    curr = head
    size = 0
    while curr:
        size += 1
        curr = curr.next
    return size


def get_start_node(head, index):
    curr = head
    while index > 0:
        curr = curr.next
        index -= 1
    return curr


def get_intersection_node(head_a, head_b):
    size_a = find_size(head_a)
    size_b = find_size(head_b)
    if size_a > size_b:
        curr_a = get_start_node(head_a, size_a - size_b)
        curr_b = head_b
    else:
        curr_a = head_a
        curr_b = get_start_node(head_b, size_b - size_a)
    while curr_a:
        if curr_a == curr_b:
            return curr_a
        curr_a = curr_a.next
        curr_b = curr_b.next


def get_intersection_node2(head_a, head_b):
    """
    2 pointer approach
    """
    pointer_a = head_a
    pointer_b = head_b
    while pointer_a is not pointer_b:
        # if either pointer hits the end, switch head and continue the second traversal,
        # if not hit the end, just move on to next
        pointer_a = head_b if pointer_a is None else pointer_a.next
        pointer_b = head_a if pointer_b is None else pointer_b.next
    return pointer_a


def create_linked_lists_intersected(head1, head2, index):
    # find last node for head2
    curr = head2
    while curr.next:
        curr = curr.next
    last_node_head2 = curr

    # find node under the given index
    curr = head1
    while index > 0:
        curr = curr.next
        index -= 1
    index_node = curr
    last_node_head2.next = index_node


ll1 = LinkedList()
lst = [2, 4, 6, 8, 0, 1, 3, 5, 7, 9]
for el in lst:
    ll1.addAtTail(el)
lst = [-1, 0, 1, 5, 10]
ll2 = LinkedList()
for el in lst:
    ll2.addAtTail(el)

create_linked_lists_intersected(ll1.head, ll2.head, 3)
ll1.print_linked_list()
ll2.print_linked_list()
result = get_intersection_node2(ll1.head, ll2.head)
print("Lists intersect in: ", result.value)
print("-**-" * 20)

ll1 = LinkedList()
lst = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
for el in lst:
    ll1.addAtTail(el)
lst = [5, 10, -1, 0, 1]
ll2 = LinkedList()
for el in lst:
    ll2.addAtTail(el)

create_linked_lists_intersected(ll1.head, ll2.head, 4)
ll1.print_linked_list()
ll2.print_linked_list()
result = get_intersection_node2(ll1.head, ll2.head)
print("Lists intersect in: ", result.value)
print("-**-" * 20)


ll1 = LinkedList()
lst = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
for el in lst:
    ll1.addAtTail(el)
ll2 = LinkedList()
lst = [5, 10, -1, 0, 1]
for el in lst:
    ll2.addAtTail(el)

create_linked_lists_intersected(ll1.head, ll2.head, 1)
ll1.print_linked_list()
ll2.print_linked_list()
result = get_intersection_node2(ll1.head, ll2.head)
print("Lists intersect in: ", result.value)

