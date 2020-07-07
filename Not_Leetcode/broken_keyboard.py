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
from LinkedList.singly_linked_list.design_linked_list import LinkedList


def broken_keyboard(text):
    """
    Complexity:
    O(n) - if there's no special characters '[' and ']'
    or all these characters are only at the beginning or the end

    O(m*n) - if special characters '[' and ']' are met in the text

    """
    ll = LinkedList()
    n = len(text)
    i = 0
    while i < n:
        if text[i] not in ['[', ']']:
            ll.addAtTail(text[i])
        else:
            j = 0
            i += 1
            while text[i] != ']' and i < n:
                if text[i] == '[':
                    break
                ll.addAtIndex(j, text[i])
                j += 1
                i += 1
        i += 1
    # ll.print_linked_list()
    res = ""
    curr = ll.head
    while curr:
        res += curr.value
        curr = curr.next
    return res


print(broken_keyboard("This_is_a_[Beiju]_text"))
print(broken_keyboard("[[]][][]Happy_Birthday_to_Tsinghua_University"))
print(broken_keyboard("Happy_Birthday_to_Tsinghua_University[[]][][]"))
print(broken_keyboard("Happy_Birthday_to_Tsinghua_[[]][][]_University"))

assert broken_keyboard("This_is_a_[Beiju]_text") == "BeijuThis_is_a__text"
assert broken_keyboard("[[]][][]Happy_Birthday_to_Tsinghua_University") == "Happy_Birthday_to_Tsinghua_University"
assert broken_keyboard("[Happy]_Birthday_to_Tsinghua_University") == "Happy_Birthday_to_Tsinghua_University"
assert broken_keyboard("Happy_Birthday_[Tsinghua_University]") == "Tsinghua_UniversityHappy_Birthday_"
assert broken_keyboard("There_are_[several]_test_cases") == "severalThere_are__test_cases"