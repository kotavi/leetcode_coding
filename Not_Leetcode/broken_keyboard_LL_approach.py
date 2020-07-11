"""
11988 Broken Keyboard (a.k.a. Beiju Text)
You're typing a long text with a broken keyboard. Well it's not so badly broken.
The only problem with the keyboard is that sometimes the "home" key or the "end" key gets automatically pressed (internally).
You're not aware of this issue, since you’re focusing on the text and did not even turn on the
monitor! After you finished typing, you can see a text on the screen (if you turn on the monitor).
In Chinese, we can call it Beiju. Your task is to find the Beiju text.
Input
There are several test cases.
Each test case is a single line containing at least one and at most 100,000 letters,
underscores and two special characters '[' and ']'.
'[' means the "Home" key is pressed internally, and ']' means the "End" key is pressed internally.
The input is terminated by end-of-file (EOF).
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.curr = None

    def print_list(self):
        curr = self.head
        while curr:
            print("{}".format(curr.data), end=" --> ")
            curr = curr.next
        print()

    def add_at_tail(self, value):
        """
        Case1: when LL is empty, so the head,
            tail and curr will point to the new node
        Case2: when LL is not empty,
            then tail and curr will move to the new node added to the end of LL
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.curr = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.curr = self.tail

    def add_at_head(self, value):
        """
        Case1: when LL is empty, so the head,
            tail and curr will point to the new node
        Case2: when LL is not empty,
            then new node will be added to the beginning of LL,
            head and curr will move to the new node
        :param value: value of the new node
        :return: the node that was added
        """
        new_node = Node(value)
        self.curr = self.head
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.curr = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.curr = self.head

    def add_after_current(self, value):
        """
        Case1: curr and tail point to the same node
        Case2: curr points to a node somewhere at the beginning of the LL
        """
        new_node = Node(value)
        new_node.next = self.curr.next
        self.curr.next = new_node
        if self.curr == self.tail:
            self.tail = new_node
        self.curr = new_node


def broken_keyboard(text):
    ll = LL()
    n, i = len(text), 0
    while i < n:
        if text[i] not in ['[', ']']:
            ll.add_at_tail(text[i])
        else:
            j = 0
            i += 1
            while i < n and text[i] != ']':
                if text[i] == ']':
                    break
                elif text[i] == '[':
                    j = 0
                    i += 1
                if j == 0:
                    ll.add_at_head(text[i])
                else:
                    ll.add_after_current(text[i])
                j += 1
                i += 1
        i += 1
    # ll.print_list()
    res = ""
    curr = ll.head
    while curr:
        res += curr.data
        curr = curr.next
    print(res)
    return res


assert broken_keyboard("This_is_a_[Beiju]_text") == "BeijuThis_is_a__text"
assert broken_keyboard("This_is_a_text_[Beiju]") == "BeijuThis_is_a_text_"
assert broken_keyboard("[[]][][]Happy_Birthday_to_Tsinghua_University") == "Happy_Birthday_to_Tsinghua_University"
assert broken_keyboard("[Happy]_Birthday_to_Tsinghua_University") == "Happy_Birthday_to_Tsinghua_University"
assert broken_keyboard("[123]_hello") == "123_hello"
assert broken_keyboard("[123_hell]o]") == "123_hello"
assert broken_keyboard("Happy_Birthday_[Tsinghua_University]") == "Tsinghua_UniversityHappy_Birthday_"
assert broken_keyboard("There_are_[123[456[789]_numbers") == "789456123There_are__numbers"
