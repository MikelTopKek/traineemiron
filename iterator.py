class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# numbers = PowTwo(3)
#
# n = iter(numbers)
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))

# for n in numbers:
#     print(n)

import time
from datetime import datetime


def tempo():
    full_data = range(0, 100)
    start_pos = 0
    end_pos = 10
    step = 5
    data = full_data[start_pos: end_pos]

    while data:
        yield data
        start_pos += step
        end_pos += step
        data = full_data[start_pos: end_pos]


for n in tempo():
    print(n)

# n = iter(tempo())
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))


# print(next(tempo()))
# print(next(tempo()))
# print(next(tempo()))
# print(next(tempo()))

