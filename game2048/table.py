import random
import os


def dec1(func):
    def clear(self):
        os.system('CLS')
        func(self)
    return clear


class Table:
    def __init__(self, number):
        self.table = [0]*number
        for i in range(number):
            self.table[i] = [0]*number
        self.number = number

    @dec1
    def display(self):
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                print(self.table[i][j], end=" ")
            print()

    def start(self):
        self.table[random.randint(0, self.number-1)][random.randint(0, self.number-1)] = 2


