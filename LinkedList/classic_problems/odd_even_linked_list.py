"""
See https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/

Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place.
The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
    Input: 1->2->3->4->5->NULL
    Output: 1->3->5->2->4->NULL

Example 2:
    Input: 2->1->3->5->6->4->7->NULL
    Output: 2->3->6->7->1->5->4->NULL

Constraints:
    The relative order inside both the even and odd groups should remain as it was in the input.
    The first node is considered odd, the second node even and so on ...
    The length of the linked list is between [0, 10^4].
"""
from LinkedList.singly_linked_list.design_linked_list import LinkedList


def odd_even_list(head):
    if not head:
        return head
    even = head  # start from head, index = 0
    odd = head.next  # start from element with index = 1
    odd_head = odd  # kep track of the odd list

    while even.next and odd.next:
        even.next = even.next.next
        even = even.next
        odd.next = odd.next.next
        odd = odd.next

    even.next = odd_head  # connect list with even indices with list with odd indices

    return head


tests = [[], [1, 2], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]]

for a_test in tests:
    ll = LinkedList()
    for el in a_test:
        ll.addAtTail(el)
    print("Initial LL     : ", end="")
    ll.print_linked_list()
    odd_even_list(ll.head)
    print("Transformed LL : ", end="")
    ll.print_linked_list()
    print()
