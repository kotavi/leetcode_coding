"""
See https://www.hackerrank.com/challenges/simple-text-editor/problem

In this challenge, you must implement a simple text editor.
Initially, your editor contains an empty string, S.
You must perform Q operations of the following 4 types:

1. append(W) - Append string W to the end of S.
2. delete(k) - Delete the last k characters of S.
3. print(k) - Print the kth character of S.
4. undo() - Undo the last (not previously undone) operation of type 1 or 2,
reverting S to the state it was in prior to that operation.

Sample input:
8
1 abc
3 3
2 3
1 xy
3 2
4
4
3 1

Sample output:
c
y
a
"""


class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def push(self, value):
        self.items.append(value)
        self.size += 1

    def add(self, data):
        for item in data:
            self.push(item)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.items.pop()

    def delete(self, num):
        deleted_str = ""
        for _ in range(num):
            value = self.items.pop()
            deleted_str = value + deleted_str
        return deleted_str

    def is_empty(self):
        return self.size == 0


def undo(stack1, stack2):
    cmd, s = stack1.pop()
    n = len(s)
    if cmd == '1':
        for _ in range(n):
            stack2.pop()
    if cmd == '2':
        for i in range(n):
            stack2.push(s[i])


if __name__ == "__main__":
    res_stack = Stack()
    undo_stack = Stack()  # temp stack to store the recent operations of 1/2 types
    expected_output = []
    N = int(input().strip())
    for _ in range(N):
        inp = input().strip().split()
        if inp[0] == '1':
            res_stack.add(inp[1])
            undo_stack.push(inp)
        elif inp[0] == '2':
            s = res_stack.delete(int(inp[1]))
            undo_stack.push([inp[0], s])
        elif inp[0] == '3':
            expected_output.append(res_stack.items[int(inp[1]) - 1])
        elif inp[0] == '4':
            undo(undo_stack, res_stack)

    for item in expected_output:
        print(item)

    print(res_stack.items)
    print(undo_stack.items)


