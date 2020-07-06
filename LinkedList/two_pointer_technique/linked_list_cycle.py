"""
https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.
"""
from LinkedList.singly_linked_list.design_linked_list import LinkedList


class TwoPointerTechnique(LinkedList):

    def has_cycle(self):
        """
        Approach:
        Use two pointer technique: slow pointer moves with +1 step forward,
        fast pointer moves with +2 steps forward.
        If there is a cycle the fast pointer will catch up with slow pointer
        :return: True if there is a cycle in the LinkedList
                 False if there is no cycle in the LinkedList
        """
        slow = fast = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    ll = TwoPointerTechnique()
    ll.addAtTail(2)
    ll.addAtTail(3)
    ll.addAtTail(13)
    ll.addAtTail(-1)

    print(ll.has_cycle())

