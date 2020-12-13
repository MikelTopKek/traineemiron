import random
import os


def dec1(func):
    def clear(self):
        os.system('CLS')
        func(self)
    return clear


"""
x,y - coordinates of the cell, into which we write a new number
on start we put a number into a random cell123
"""


class Table:
    def __init__(self, number) -> None:
        self.table = [0]*number
        for i in range(number):
            self.table[i] = [0]*number
        self.number = number
        self.x = random.randint(0, self.number - 1)
        self.y = random.randint(0, self.number - 1)

    @dec1
    def display(self) -> None:
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                print(self.table[i][j], end=" ")
            print()

    def start(self) -> None:
        while self.table[self.x][self.y] != 0:
            self.x = random.randint(0, self.number - 1)
            self.y = random.randint(0, self.number - 1)
        self.table[self.x][self.y] = 2

    @dec1
    def move_down(self):
        for i in range(len(self.table)):



