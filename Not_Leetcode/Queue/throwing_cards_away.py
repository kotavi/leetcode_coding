"""
Given is an ordered deck of n cards numbered 1 to n with card 1 at the top and card n at the bottom.
The following operation is performed as long as there are at least two cards in the deck:
Throw away the top card and move the card that is now on the top of the deck to the bottom of the deck.
Your task is to find the sequence of discarded cards and the last, remaining card.
Input
    Each line of input (except the last) contains a number n ≤ 50.
    The last line contains '0' and this line should not be processed.
Output
    For each number from the input produce two lines of output.
    The first line presents the sequence of dis- carded cards, the second line reports the last remain- ing card. No line will have leading or trailing spaces. See the sample for the expected format.
Sample Input
    7 19 10 6 0
Sample Output
    Discarded cards: 1, 3, 5, 7, 4, 2
    Remaining card: 6
    Discarded cards: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 4, 8, 12, 16, 2, 10, 18, 14
    Remaining card: 6
    Discarded cards: 1, 3, 5, 7, 9, 2, 6, 10, 8
    Remaining card: 4
    Discarded cards: 1, 3, 5, 2, 6
    Remaining card: 4
"""


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
        return first_node

    def print_queue(self):
        curr = self.head
        while curr:
            print("{}".format(curr.val), end=" --> ")
            curr = curr.next
        print()


if __name__ == '__main__':
    nums = [7, 19, 10, 6]

    for num in nums:
        queue = Queue()  # queue with initial deck of cards
        discarded_queue = Queue()  # queue for discarded cards
        for i in range(1, num+1):
            queue.enqueue(i)  # appending cards to the queue
        print("Initial deck of cards: ", end="")
        queue.print_queue()
        for i in range(queue.size - 1):
            # remove the top element from the queue and append it to discarded_queue
            discarded_queue.enqueue(queue.dequeue().val)
            # # remove the top element from the queue and append it to the current queue
            queue.enqueue(queue.dequeue().val)

        print("Discarded cards: ", end="")
        discarded_queue.print_queue()
        print("Remaining card: ", end="")
        queue.print_queue()

        print("-*--" * 10)
