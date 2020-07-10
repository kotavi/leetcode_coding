"""
See https://www.chegg.com/homework-help/questions-and-answers/basic-c-program-using-stack-need-cpp-file-background-famous-railway-station-poppush-city-c-q26344457
"""


class Stack:

    def __init__(self):
        self.items = []
        self.size = 0

    def __repr__(self):
        return "Stack object: {}".format(self.items)

    def push(self, value):
        self.items.append(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.items.pop()

    def peek(self):
        if self.size == 0:
            return None
        return self.items[-1]


def validate(n, expected_result):
    """
    Notes:
    1. Every element from 1,...,N should be pushed to station_stack
    2. after element is pushed it's compared to the element in the expected output
        - if values match: element is popped from station_stack and pushed to B_stack
            - match other top values in station_stack to the next values of the expected output
    3. compare expected_result with items of B_stack
    """
    station_stack = Stack()
    b_stack = Stack()
    j = 0  # to traverse expected_result
    # train is coming from the track A
    # i are the coaches, starting with 1
    for i in range(1, n + 1):  # loop through 1...N
        station_stack.push(i)
        if station_stack.peek() == expected_result[j]:
            b_stack.push(station_stack.pop())
            j += 1  # move to the next element in expected_result

            # check if the other elements from station_stack match to
            # the next elements of expected_result
            while station_stack.size > 0:
                if station_stack.peek() == expected_result[j]:
                    b_stack.push(station_stack.pop())
                    j += 1
                # if the next value in expected_result becomes smaller
                # then value of the top of the stack, it means that
                # next values in station_stack will proceed increasing
                # So there is no point to continue
                elif expected_result[j] < station_stack.peek():
                    return False
                else:
                    break
    return b_stack.items == expected_result


print(validate(6, [6, 5, 4, 3, 2, 1]))  # True
print(validate(5, [5, 4, 1, 2, 3]))  # False
print(validate(7, [3, 5, 4, 6, 7, 2, 1]))  # True
print(validate(7, [1, 2, 3, 4, 5, 6, 7]))  # True
print(validate(10, [1, 4, 3, 8, 7, 6, 10, 9, 5, 2]))  # True

# True
print(validate(99, [2, 6, 5, 9, 8, 7, 4, 3, 12, 11, 13, 10, 17, 18, 20, 22, 21, 25, 31, 30, 32, 33, 29, 34, 35, 28,
                    41, 40, 42, 39, 43, 38, 46, 47, 48, 51, 50, 49, 45, 52, 44, 56, 55, 54, 53, 37, 57, 36, 58, 59,
                    60, 27, 26, 61, 62, 24, 23, 19, 16, 65, 66, 64, 67, 68, 63, 15, 75, 74, 73, 72, 76, 77, 79, 80,
                    82, 83, 81, 85, 88, 87, 94, 93, 95, 92, 96, 97, 91, 90, 99, 98, 89, 86, 84, 78, 71, 70, 69, 14, 1]))

# False
# looping is stopped when b_stack is [2, 6, 5, 9, 8, 7, 4, 3, 12, 13]
# and station_stack is [1, 10, 11]
# next element in expected_result is 10 but next element in station_stack is 11
# meaning that we won't be able to find 10 in station_stack after 11
print(validate(99, [2, 6, 5, 9, 8, 7, 4, 3, 12, 13, 10, 17, 18, 20, 22, 21, 25, 31, 30, 32, 33, 29, 34, 35, 28,
                    41, 40, 42, 39, 43, 38, 46, 47, 11, 48, 51, 50, 49, 45, 52, 44, 56, 55, 54, 53, 37, 57, 36, 58, 59,
                    60, 27, 26, 61, 62, 24, 23, 19, 16, 65, 66, 64, 67, 68, 63, 15, 75, 74, 73, 72, 76, 77, 79, 80,
                    82, 83, 81, 85, 88, 87, 94, 93, 95, 92, 96, 97, 91, 90, 99, 98, 89, 86, 84, 78, 71, 70, 69, 14, 1]))
