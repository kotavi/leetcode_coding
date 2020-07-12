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

    def move_curr_front(self):
        self.curr = self.head

    def move_curr_end(self):
        self.curr = self.tail

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
    prev_ch = ''  # keep track of '[' and ']' changing
    # to know when enter character at the head,
    # when flag is False - enter character after the current
    flag = True
    for ch in text:
        if ch not in ['[', ']']:
            if prev_ch == '':
                ll.add_at_tail(ch)
            elif prev_ch == '[' and flag:
                ll.add_at_head(ch)
                # after ch was added at the head the following ch will be added after curr
                flag = False
            elif prev_ch == '[' and not flag:
                ll.add_after_current(ch)
            elif prev_ch == ']':
                ll.add_at_tail(ch)
        # move cursor depending on ']' abd '[' characters
        elif ch == '[':
            prev_ch = '['
            flag = True
            ll.move_curr_front()
        elif ch == ']':
            prev_ch = ']'
            ll.move_curr_end()
    res = ""
    curr = ll.head
    while curr:
        res += curr.data
        curr = curr.next
    print(res)
    return res


assert broken_keyboard("[[]][][]Happy_Birthday_to_Tsinghua_University") == "Happy_Birthday_to_Tsinghua_University"
assert broken_keyboard("[123]_hello[[][][]]") == "123_hello"

assert broken_keyboard("This_is_a_[Beiju]_text") == "BeijuThis_is_a__text"
assert broken_keyboard("[Happy]_Birthday_to_Tsinghua_University") == "Happy_Birthday_to_Tsinghua_University"
assert broken_keyboard("[123_hell]o]") == "123_hello"
assert broken_keyboard("Happy_Birthday_[Tsinghua_University]") == "Tsinghua_UniversityHappy_Birthday_"
assert broken_keyboard("There_are_[123[456[789]_numbers") == "789456123There_are__numbers"
assert broken_keyboard("1[2[3[4[5[6[7[8[9[0") == "0987654321"

assert broken_keyboard("1[[2[[3[[4[[5[[6[[7[[8[[9[[0") == "0987654321"
assert broken_keyboard("1[]2[]3[]4[]5[]6[]7[]8[]9[]0") == "1234567890"
assert broken_keyboard("[[[1[2[3]]]") == "321"
assert broken_keyboard("1]2]3[[[4") == "4123"
assert broken_keyboard("[[u[]a_Un") == "ua_Un"

assert broken_keyboard("a_[b_[c_[d_[e_[f_[g") == "gf_e_d_c_b_a_"
assert broken_keyboard("H[a[pp]y]_Bir[t]hd[a]y[_[Tsi[ng]h[[u[]a_Un[]i[]v[e[rsity]") == \
       "rsityeungTsi_atppaHy_Birhdyha_Univ"
