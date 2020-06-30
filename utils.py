from random import randint


def generate_array(start, end, size):
    return [randint(start, end) for _ in range(size)]


print(generate_array(10, 10000, 200))
